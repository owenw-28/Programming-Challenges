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
        home_shots = row[7]
        away_shots = row[8]
        home_shots_target = row[9]
        away_shots_target = row[10]
        home_foul = row[11]
        away_foul = row[12]
        
        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0,0,0] #win,draw,loss,gd,points,accuracy,fouls per game

        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0,0,0]

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
        dictionary[home][5] += (int(home_shots_target)/int(home_shots))/38
        dictionary[away][5] += (int(away_shots_target)/int(away_shots))/38
        dictionary[home][6] += (int(home_foul))/38
        dictionary[away][6] += (int(away_foul))/38
    return(dictionary)

def ref_stats(rows):
    ref_dict = {}
    for row in rows:
        ref = row[6]
        home_yellow = row[15]
        away_yellow = row[16]
        home_red = row[17]
        away_red = row[18]

        if ref not in ref_dict:
            ref_dict[ref] = [0,0,0]

        ref_dict[ref][0] += int(home_yellow) + int(away_yellow)
        ref_dict [ref][1] += int(home_red) + int(away_red)
    ref_dict[ref][2] = int(ref_dict[ref][0]) + (int(ref_dict[ref][1]*2))

    return(ref_dict)
        
            
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    table = (process_results(file_contents))
    referee = (ref_stats(file_contents))
    print("Team             W   D   L   GD  P   Shot Acc  F/G")
    print("")
    for key, value in sorted(table.items(), key=lambda items: items[1][4], reverse=True):
        print(key,7*" ", value[0],"|",value[1],"|",value[2],"|",value[3],"|",value[4],"|",round(value[5],3),"|",round(value[6],2))
        
    print("")
    print("Referee         Y    R")
    print("")
    for key in referee.items():
        print (key[0],7*" ", key[1][0],"|",key[1][1])

    sorted_accuracy = sorted(table.items(), key=lambda e: e[1][5])
    sorted_fouls = sorted(table.items(), key=lambda e: e[1][6])
    sorted_referee = sorted(referee.items(), key=lambda e: e[1][2])
    
print("")
print(f"Most accurate team: {sorted_accuracy[19][0]}")
print(f"Least accurate team: {sorted_accuracy[0][0]}")
print(f"Dirtest team: {sorted_fouls[19][0]}")
print(f"Cleanest team: {sorted_fouls[0][0]}")
print(f"Referee with highest card average: {sorted_referee[19][0]}")
print(f"Referee with lowest card average: {sorted_referee[0][0]}")
