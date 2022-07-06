from sportsipy.nhl.teams import Teams
from sportsipy.fb.team import Team
from sportsipy.nba.teams import Teams
from sportsipy.mlb.teams import Teams
from sportsipy.ncaab.schedule import Schedule


# prints an ncaa team's current schedule
def ncaa_team_schedule():
    team = input("Enter the NCAA team's name ")
    schedule = Schedule(team)
    for game in schedule:
        print(game.date)

#prints the schedule of selected nba team
def nba_schedule(team):
    from sportsipy.nba.schedule import Schedule
    schedule = Schedule(team)
    for i in schedule:
        print(i.date)

#print nba team roster
def nba_roster(team):
    from sportsipy.nba.roster import Player
    nba_team = Roster(team)
    for player in nba_team.players:
        print(player.name)
        #prints each player on the team 

# prints which team had the most wins in a certain year
def print_most_wins(year, wins):
    most_wins = max(wins, key=wins.get)
    print('%s: %s - %s' % (year, wins[most_wins], most_wins))

#

# our main menu
end = 0
while end == 0:
    print("Type the number of the sport you want")
    print("1. NCAA - 2. NBA - 3. NHL - 4. FB - 5. MLB")
    text = input("")

    if text == '1':
        print("Choose the number of your fringe question")
        print("1. What's this year's schedule for BLANK team?")
        text = input("")
        if text == '1':
            ncaa_team_schedule()
            text = input("Want to exit? press 1 ")
            if text == '1':
                end = 1
    #if they choose 2, they choose nba            
    elif text == '2':
        print("Choose your team")
        from sportsipy.nba.teams import Teams
        teams = Teams()
        for i in teams:
            print(team.name)
        name = input("")
        print(f"1. What's this year's schedule for {name} team? \n 2. Whats the current roster?")
        #prompted a question- if 1 print schedule, if 2 print roster
        if text == '1':
            nba_schedule(team)
            text = input("Want to exit? press 1 ")
            if text == '1':
                end = 1
        if text == '2':
            nba_roster(team)
            text = input("Want to exit? press 1 ")
            if text == '1':
                end = 1
                
    elif text == '3':
        print("Choose the number of your fringe question")
        print("1. What's this year's schedule for BLANK team?")
        text = input("")
        if text == '1':
