import random
import sqlite3
from sqlite3 import Error

from sportsipy.nba.roster import Roster
from sportsipy.nba.roster import Player
from sportsipy.nhl.teams import Teams
from sportsipy.fb.team import Team
from sportsipy.nba.teams import Teams
from sportsipy.mlb.teams import Teams
from sportsipy.ncaab.schedule import Schedule
from sportsipy.nba.teams import Teams

# puts random int from 1 - 5 into a database and then returns the random int
# in string format.
def get_random_int_from_database():
    # create sql lite database n' stuff
    # define connection and cursor
    connection = sqlite3.connect('holding.db')

    cursor =  connection.cursor()

    # create stores table
    command1 = """CREATE TABLE IF NOT EXISTS
    top(store_id INTEGER PRIMARY KEY, rank INTEGER)"""

    cursor.execute(command1)

    # add to top
    # get a random integer between 1 and 5
    rand = str(random.randint(1, 2))
    cursor.execute(f"INSERT INTO top VALUES (1, {rand})")

    # get results
    cursor.execute("SELECT rank FROM top")
    results = cursor.fetchall()
    number = results[0][0]
    return str(number)


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


# our main menu
end = 0
while end == 0:
        print("Choose the number of your fringe question")
        print("1. What's this year's schedule for BLANK team in the NCAA?\n"
              "2. NBA Section\n"
              "10. I'm feeling lucky")
        text = input("")
        if text == '10':
            text = get_random_int_from_database()

        if text == '1':
            ncaa_team_schedule()
            text = input("Want to exit? press 1. If not, press 0")
            if text == '1':
                end = 1

        # if they choose 2, they choose nba
        # input must be the team abbreviation! So GSW for golden state warriors, etc.
        if text == '2':
            print("Input team's abbreviation")

            team = input("")
            print(f"1. What's this year's schedule for the {team} team? \n2. Whats the current roster?")
            # prompted a question- if 1 print schedule, if 2 print roster
            text = input("")
            if text == '1':
                nba_schedule(team)
                text = input("Want to exit? press 1. If not, press 0")
                if text == '1':
                    end = 1
            if text == '2':
                nba_roster(team)
                text = input("Want to exit? press 1. If not, press 0")
                if text == '1':
                    end = 1