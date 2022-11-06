import csv 
from pathlib import Path

csv_file = Path("one_row.csv")
csv_file2 = Path("blank.csv")
csv_file3 = Path("Premier 16-17.csv")

def check_file_exists(csv_file,): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                
            for row in reader:
                csv_contents.append(row)
    return csv_contents
        
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
