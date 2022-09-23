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
            dictionary[home][1] +=1
            dictionary[home][4] +=3
            dictionary[away][2] +=1
            home_goaldiff[3] = home_goaldiff[3] + (homegoals - awaygoals)
            away_goaldiff[3] = away_goaldiff[3] + (awaygoals - homegoals)
        else:
            dictionary[away][1] +=1
            dictionary[away][4] +=3
            dictionary[home][2] +=1
            home_goaldiff[3] = home_goaldiff[3] + (homegoals - awaygoals)
            away_goaldiff[3] = away_goaldiff[3] + (awaygoals - homegoals)
    print(dictionary)
            
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    print(process_results(file_contents))


