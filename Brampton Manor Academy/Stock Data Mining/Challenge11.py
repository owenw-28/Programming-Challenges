import csv 
from pathlib import Path

csv_file = Path("AAPL.csv")


def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)                   
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def process_data(rows):
    dictionary = {}
    for row in rows:
        

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = (process_data(file_contents))
