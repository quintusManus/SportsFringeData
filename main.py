import sqlite3

from sportsipy.nba.roster import Roster
from sportsipy.nba.teams import Teams
from sportsipy.nba.teams import Teams


# gets random value from database. Returns string
def get_random_int_from_database():
    # create sql lite database n' stuff
    # define connection and cursor
    connection = sqlite3.connect('holding.db')

    cursor = connection.cursor()

    # create stores table
    command1 = """CREATE TABLE IF NOT EXISTS
    top(store_id INTEGER PRIMARY KEY, rank INTEGER)"""

    cursor.execute(command1)

    # get random row in the database (there's 1 through 5)
    cursor.execute("SELECT * FROM top ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchall()
    number = results[0][0]
    return str(number)


# prints the schedule of selected nba team
def nba_schedule(team):
    from sportsipy.nba.schedule import Schedule
    schedule = Schedule(team)
    for i in schedule:
        print(i.date)


# print nba team roster
def nba_roster(team):
    from sportsipy.nba.roster import Player
    nba_team = Roster(team)
    for player in nba_team.players:
        print(player.name)
        # prints each player on the team


# prints which team had the most wins in a certain year
def print_most_wins(year, wins):
    most_wins = max(wins, key=wins.get)
    print('%s: %s - %s' % (year, wins[most_wins], most_wins))


# our main menu
end = 1
while end == 1:
    print("Choose the number of your question")
    print(f"1. What's this year's schedule for BLANK team? \n2. Whats the current roster "
          f"for BLANK team?\n"
          f"10. I'm feeling lucky")

    # prompted a question- if 1 print schedule, if 2 print roster
    text = input("")
    # If they press I'm feeling lucky, get the random int
    if text == '10':
        text = get_random_int_from_database()

    if text == '1':
        # input must be the team abbreviation! So GSW for golden state warriors, etc.
        print("Input team's abbreviation")
        team = input("")
        nba_schedule(team)
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0

    if text == '2':
        # input must be the team abbreviation! So GSW for golden state warriors, etc.
        print("Input team's abbreviation")
        team = input("")
        nba_roster(team)
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
