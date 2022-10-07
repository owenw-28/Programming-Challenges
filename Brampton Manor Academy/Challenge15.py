import csv
from pathlib import Path

import urllib.request
import html

csv_file = Path("south.csv")

def read_csv(csv_file):
     csv_contents = []
     with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")                   
        for row in reader:
            csv_contents.append(row)
     return csv_contents
    ## read the specified csv file just like Challenge 10
    
def read_html(html_file):
    with open(html_file) as htmlfile:
        html = htmlfile.read()
    return html
    ## read a html file as a regular file

def process(csv, html):
    i = 0
    position = html.find('background-image: url("link1");')
    position = position.replace("link1",csv[i,0])
    while position !=-1 and count<=5:
        start = html.find('background-image: url("')
        stop = html.find('");',start)
        html[start:stop] = csv[i,0]
        i += 1
        
    ## replace link1...link5 in html with corresponding values from csv
    ## Similarly do for initials1...intitials5 and name1...name5
    
def write_html(path, html):
    ## write the new contents into an html file

 
if __name__ == "__main__":
    csv = read_csv("south.csv")
    html = read_html("south.html")
    html = process(csv, html)
    write_html("south_final.html", html)

