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
from sportsipy.nba.player import AbstractPlayer


# puts random int from 1 - 5 into a database and then returns the random int
# in string format.
def get_random_int_from_database():
    # create sql lite database n' stuff
    # define connection and cursor
    connection = sqlite3.connect('holding.db')

    cursor = connection.cursor()

    # create stores table
    command1 = """CREATE TABLE IF NOT EXISTS
    top(store_id INTEGER PRIMARY KEY, rank INTEGER)"""

    cursor.execute(command1)

    # add to top
    # get a random integer between 1 and 7
    rand = str(random.randint(1, 7))
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

# def player_id(self):
#         """
#         Returns a ``string`` of the player's ID on sports-reference, such as
#         'hardeja01' for James Harden.
#         """
#         return self._player_id

def lebron_blocks():
        player_name=input("Enter player's name:")
        lebron_james= player_name.player_id()
        print(f'{lebron_james.name} has a block percentage of {lebron_james.block_percentage}.' )  #Print Lebron James block percentage for the year. 

def steph_three_pointers():
        steph_curry=Player('curryst01')
        print(f'{steph_curry.name} made {steph_curry._three_pointers} this season.') # Print steph curry's three pointers

def gsw_steals():
    warriors= Team('GSW')
    print(f'{warriors.name}had {warriors.steals}this season.') #prints gsw's steals for the season

def lebron_points(): 
        lebron_james = Player('jamesle01')
        print(f'{lebron_james.name} scored {lebron_james._points} this season.' )  #Print Lebron James points for the season. 

def lebron_salary():
        lebron_james = Player('jamesle01')
        print(f'{lebron_james.name} makes {lebron_james.salary} in a year.' )  #Print Lebron James salary for the year. 



# our main menu
end = 1
while end == 1:
    print("Choose the number of your question")
    print("1.What's this year's schedule for _____ team?")
    print("2.How many blocks does Lebron James have this season?")
    print("3.What is the roster for ___ team this season?")
    print("4.How many 3-pointers did Stephen Curry make this season?")
    print("5.How many steals did the Golden State warriors achieve this season?")
    print("6.How many points does Lebron James have this season?")
    print("7.How much does Lebron get paid?")
    print("10. I'm feeling lucky.")

    # prompted a question
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
    if text =='2':
        lebron_blocks()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
    if text == '3':
    # input must be the team abbreviation! So GSW for golden state warriors, etc.
        print("Input team's abbreviation")
        team = input("")
        nba_roster(team)
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
             end = 0
    if text == '4':
        steph_three_pointers()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
    if text == '5':
        gsw_steals()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
    if text == '6':
        lebron_points()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
    if text == '7':
        lebron_salary()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0



