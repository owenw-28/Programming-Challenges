import csv
from pathlib import Path

csv_file = Path("AAPL.csv")


def read_csv(csv_path):
    csv_array = []
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            csv_array.append(row)
    return csv_array


def process_results(csv):
    dictionary = {}
    year_month_list = []

    for row in csv:
        date = row[0].split('-')
        year_month = date[0] + '-' + date[1]

        if year_month not in year_month_list:
            dictionary[year_month] = [0,0,0]  #Adj Close*Volume, Volume, index[0]/index[1]
            year_month_list.append(year_month)

        if year_month == (row[0])[:-3]:
            dictionary[year_month][0] = float(row[5])
            dictionary[year_month][1] = float(row[6])
            dictionary[year_month][2] = float(row[5]) * float(row[6])

    sorted_dict = list(sorted(dictionary.items(), reverse=True, key=lambda e: e[1]))
    return sorted_dict


def result(sorted_dict):
    print("The best 6 months are:")
    for count in range(6):
        print(sorted_dict[count][0])

    print("\nThe worst 6 months are:")
    for count in range(6):
        print(sorted_dict[::-1][count][0])


if __name__ == '__main__':
    file_contents = read_csv(csv_file)
    sorted_dict = process_results(file_contents)
    result(sorted_dict)
    
