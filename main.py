from sportsipy.nhl.teams import Teams
from sportsipy.fb.team import Team
from sportsipy.nba.teams import Teams
from sportsipy.mlb.teams import Teams
from sportsipy.ncaab.schedule import Schedule

# prints an ncaa team's current schedule
def ncaa_team_schedule():
        team = input("")
        schedule = Schedule(team)
        for game in schedule:
            print(game.date)

# prints an ncaa team's turnover percentage
def ncaa_team_turnover():
        team = input("")
        for team in Teams():
            print(team.name, team.wins, team.losses)

def print_most_wins(year, wins):
    most_wins = max(wins, key=wins.get)
    print('%s: %s - %s' % (year, wins[most_wins], most_wins))

for year in range(2000, 2019):
    wins = {}
    for team in Teams(year):
        wins[team.name] = team.wins
    print_most_wins(year, wins)