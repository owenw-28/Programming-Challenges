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
    replacingList = [[0,'link'], [1, 'initials'], [2, 'name']]
    for array in replacingList:
        for i in range(0,5):
            name = array[1] + str(i+1)
            html = html.replace(name, csv[i][array[0]])
    return html

    ## replace link1...link5 in html with corresponding values from csv
    ## Similarly do for initials1...intitials5 and name1...name5

def write_html(path, html):
    with open (path, 'w') as htmlfile:
        htmlfile.write(html)
        
 
if __name__ == "__main__":
    csv = read_csv("south.csv")
    html = read_html("south.html")
    html = process(csv, html)
    write_html("south_final.html", html)
