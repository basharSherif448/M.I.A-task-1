def process_match(standings,team_1,team_2,team_1_goals,team_2_goals):
    #played matches
    standings[team_1]["P"]+=1
    standings[team_2]["P"]+=1 
    #win and losses
    if team_1_goals>team_2_goals:
        standings[team_1]["W"]+=1
        standings[team_2]["L"]+=1
    elif team_1_goals<team_2_goals:
        standings[team_2]["W"]+=1
        standings[team_1]["L"]+=1
    else:
        standings[team_1]["D"] += 1
        standings[team_2]["D"] += 1    
    #Goals for both teams
    standings[team_1]["GF"]+=team_1_goals    
    standings[team_2]["GF"]+=team_2_goals   
     #Goals accepted by both teams
    standings[team_1]["GA"]+=team_2_goals    
    standings[team_2]["GA"]+=team_1_goals   
    #Goal diffrences
    standings[team_1]["GD"]=standings[team_1]["GF"]-standings[team_1]["GA"]
    standings[team_2]["GD"]= standings[team_2]["GF"]-standings[team_2]["GA"]
    #POINTS
    if team_1_goals > team_2_goals:
        standings[team_1]["Pts"] += 3

    elif team_1_goals < team_2_goals:
        standings[team_2]["Pts"] += 3

    else:
        standings[team_1]["Pts"] += 1
        standings[team_2]["Pts"] += 1


def validate(score): #input validation  
    if score.count('-')!=1:
        return False
    score_list=score.split('-')
    if ( not score_list[0].isdigit() or not score_list[1].isdigit() ):
        return False

    return True

def print_standings(standings):
    sorted_teams = sorted(
        standings.items(),
        key=lambda x: (x[1]["Pts"], x[1]["GD"], x[1]["GF"]),
        reverse=True
    )

    print("Team P W D L GF GA GD Pts")

    for team, stats in sorted_teams:

        if stats["GD"] > 0:
            gd = "+" + str(stats["GD"])
        elif stats["GD"] < 0:
            gd = str(stats["GD"])
        else:
            gd = "0"

        print(
            team,
            stats["P"],
            stats["W"],
            stats["D"],
            stats["L"],
            stats["GF"],
            stats["GA"],
            gd,
            stats["Pts"]
        )
standings={
"ARG":{
    "P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,'GD':0,"Pts":0
},
"POL":{
    "P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,'GD':0,"Pts":0
},
"MEX":{
    "P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,'GD':0,"Pts":0
},
"KSA":{
    "P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,'GD':0,"Pts":0
}

}
while True:
    score = input("Enter score ARG vs MEX (format 2-0): ")  ### Match 1  ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"ARG","MEX",team1_goals,team_2goals)

while True:
    score = input("Enter score ARG vs POL (format 2-0): ")   ### Match 2 ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"ARG","POL",team1_goals,team_2goals)

while True:
    score = input("Enter score ARG vs KSA (format 2-0): ")      ### Match 3 ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"ARG","KSA",team1_goals,team_2goals)


while True:
    score = input("Enter score MEX vs POL (format 2-0): ")      ### Match 4 ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"MEX","POL",team1_goals,team_2goals)


while True:
    score = input("Enter score MEX vs KSA (format 2-0): ")      ### Match 5 ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"MEX","KSA",team1_goals,team_2goals)

while True:
    score = input("Enter score POL vs KSA (format 2-0): ")      ### Match 6 ###
    if validate(score):
        break
match1=score.split('-')
team1_goals=int(match1[0])
team_2goals=int(match1[1])
process_match(standings,"POL","KSA",team1_goals,team_2goals)

print_standings(standings)



