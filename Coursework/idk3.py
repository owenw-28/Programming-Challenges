import yfinance as yf
from datetime import date, timedelta
from datetime import datetime
import pandas_ta as pta
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_data(Company):
    data = yf.Ticker(f'{Company}')

    # get historical market data
    hist = data.history(period="1y")
    hist = hist.drop(['Dividends', 'Stock Splits'], axis=1)
    hist.reset_index(inplace=True)

    dates = []

    for i in range(len(hist['Date'])):
        date_str = str(hist['Date'][i])
        date_str = date_str[:10]
        date_format = '%Y-%m-%d'
        date_obj = datetime.strptime(date_str, date_format)
        dates.append(date_obj)

    hist['Date'] = dates
    hist = hist.set_index('Date')

    return hist


def sma_strategy(symbol, df):
    df['50d-SMA'] = df['Close'].rolling(50).mean()
    df['20d-SMA'] = df['Close'].rolling(20).mean()
    df.dropna(inplace=True)

    dates = list(df.index.values)

    print(df)

    fig = go.Figure(data=[go.Candlestick(name='Candles', x=df.index, open=df['Open'], high=df['High'],
                                         low=df['Low'], close=df['Close'])])

    fig.add_trace(go.Scatter(x=hist.index, y=df['50d-SMA'], line=dict(color='#856BE6'), name='50d-SMA'))
    fig.add_trace(go.Scatter(x=hist.index, y=df['20d-SMA'], line=dict(color='#EBE3BE'), name='20d-SMA'))

    fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark',
                      xaxis_title='Date', yaxis_title=f'{symbol} Price ($USD)', shapes = [
        dict(x0=dates[-1] , x1=dates[0] , y0=0, y1=1, xref='x', yref='paper',
             line_width=2)])

    fig.update_layout(autotypenumbers='convert types')
    fig.show()

def ema_strategy(symbol, df):
    df['EMA12'] = df['Close'].ewm(span=12).mean()
    df['EMA26'] = df['Close'].ewm(span=26).mean()
    df.dropna(inplace=True)

    dates = list(df.index.values)

    print(df)

    fig = go.Figure(data=[go.Candlestick(name='Candles', x=df.index, open=df['Open'], high=df['High'],
                                         low=df['Low'], close=df['Close'])])

    fig.add_trace(go.Scatter(x=df.index, y=df['EMA12'], line=dict(color='#856BE6'), name='12d-EMA'))
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA26'], line=dict(color='#EBE3BE'), name='26d-SMA'))

    fig.update_layout(
        title={
            'text': f'<b>Stock Price Movement with EMA for {symbol}</b>',
            'y': 0.85,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
        },
        font=dict(
            family="Arial",
            size=8,
            color='black'
        ),
        plot_bgcolor='white'

    ),

    fig.update_yaxes(title_text="<b>Stock Prices</b>")

    fig.update_xaxes(tickfont=dict(size=8))
    fig.update_xaxes(title_text="<b>Period</b>", title_font=dict(size=8), tickfont=dict(size=8))

    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=-0.1,
        y0=-0.2,
        x1=1.02,
        y1=1.0,
        line=dict(
            color="gray",
            width=1.5,
        )
    )
    fig.update_xaxes(rangeslider_visible=False)
    fig.show()

def rsi_strategy(symbol, df):
    df['RSI'] = pta.rsi(df['Close'], length=14)
    df.dropna(inplace=True)

    dates = list(df.index.values)

    print(df)

    # Create Figure
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=False, row_width=[100, 250],
        specs=[[{"secondary_y": True}], [{"secondary_y": False}]]
    )

    # Create Candlestick chart for price data
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        showlegend=False
    ), row=1, col=1, secondary_y=True,
    )


    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['RSI'],
        line=dict(color='blue', width=1),
        showlegend=False,
    ), row=2, col=1
    )
    # Add upper/lower bounds
    fig.update_yaxes(range=[-10, 110], row=2, col=1)
    fig.add_hline(y=0, col=1, row=2, line_color="red", line_width=1)
    fig.add_hline(y=100, col=1, row=2, line_color="red", line_width=1)

    # Add overbought/oversold
    fig.add_hline(y=30, col=1, row=2, line_color='gray', line_width=1, line_dash='dot')
    fig.add_hline(y=70, col=1, row=2, line_color='gray', line_width=1, line_dash='dot')

    fig.update_layout(
        title={
            'text': f'<b>Stock Price Movement with RSI for {symbol}</b>',
            'y': 0.85,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
        },
        font=dict(
            family="Arial",
            size=8,
            color='black'
        ),
        plot_bgcolor='white'

    ),

    fig.update_yaxes(title_text="<b>Stock Prices</b>", secondary_y=False, row=1, col=1, title_font=dict(size=8),
                     tickfont=dict(size=8))

    fig.update_xaxes(row=1, col=1, tickfont=dict(size=8))

    fig.update_yaxes(title_text="<b>RSI</b>", secondary_y=False, row=2, col=1, title_font=dict(size=8),
                     tickfont=dict(size=8))
    fig.update_xaxes(title_text="<b>Period</b>", row=2, col=1, title_font=dict(size=8), tickfont=dict(size=8))

    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=-0.1,
        y0=-0.2,
        x1=1.02,
        y1=1.0,
        line=dict(
            color="gray",
            width=1.5,
        )
    )
    fig.update_xaxes(rangeslider_visible=False)
    fig.layout.yaxis2.showgrid = True
    fig.show()

symbol = 'AAPL'
hist = get_data(symbol)
#sma_strategy(symbol, hist)
ema_strategy(symbol, hist)
rsi_strategy(symbol, hist)