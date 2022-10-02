students=int(input(""))
teams=int(input(""))
team_div=students//teams
req=teams*team_div
rem=students-req
print("The number of students in each team is {team_div} and left out is {rem}".format(
    team_div=team_div,rem=rem
))  
