import csv 
from pathlib import Path

csv_file = Path("Premier 16-17.csv")

        
def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)                   
        for row in reader:
            csv_contents.append(row)
    return csv_contents

    
def process_results(rows):
    dictionary = {}
    for row in rows:
        home = row[1]
        away = row[2]
        goals_home = row[3]
        goals_away = row[4]
        winner = row[5]
        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0]

        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0]

        if winner == "D":
            dictionary[home][1] +=1
            dictionary[home][4] +=1
            dictionary[away][1] +=1
            dictionary[away][4] +=1
        elif winner == "H":
            dictionary[home][0] +=1
            dictionary[home][4] +=3
            dictionary[away][2] +=1
            dictionary[home][3] += int(goals_home) - int(goals_away)
            dictionary[away][3] += int(goals_away) - int(goals_home)
        else:
            dictionary[away][0] +=1
            dictionary[away][4] +=3
            dictionary[home][2] +=1
            dictionary[home][3] += int(goals_home) - int(goals_away)
            dictionary[away][3] += int(goals_away) - int(goals_home)
    return(dictionary)
            
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    table = (process_results(file_contents))
    for key, value in sorted(table.items(), key=lambda e: e[1][4], reverse=True):
    if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    table = (process_results(file_contents))
    for key, value in sorted(table.items(), key=lambda e: e[1][4], reverse=True):
    i = 0
    for i in range (0,19):
        print(f"{key[i], {value[4]},{value[0]},{value[1]},{value[2]},{value[3]}")
        print(key, value)




