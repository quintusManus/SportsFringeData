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


# prints which team had the most wins in a certain year
def print_most_wins(year, wins):
    most_wins = max(wins, key=wins.get)
    print('%s: %s - %s' % (year, wins[most_wins], most_wins))

end = 0
while end == 0:
    print("Type the number of the sport you want")
    print("1. NCAA")
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