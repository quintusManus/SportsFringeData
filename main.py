import sqlite3

from sportsipy.nba.roster import Roster
from sportsipy.nba.roster import Player


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


def player_blocks():
    id = input("Enter player's id:\n")
    player = Player(id)
    print(
        f'{player.name} has a block percentage of {player.block_percentage}.')  # Print a player's block percentage for the year.


def player_three_pointers():
    id = input("Enter player's id:\n")
    player = Player(id)
    print(f'{player.name} made {player.three_pointers} three pointers '
          f'in their NBA career.')  # Print a player's three pointers


def player_steals():
    id = input("Enter player's id:\n")
    player = Player(id)
    print(f'{player.name} had {player.steals} steals this season.')  # prints a player's steals for their career


def player_points():
    id = input("Enter player's id:\n")
    player = Player(id)
    print(
        f'{player.name} scored {player.points} points in their NBA career.')  # Print a player's points in their NBA career.


def player_salary():
    id = input("Enter player's id:")
    player = Player(id)
    print(f'{player.name} made ${player.salary} in their career.')  # Print a player's total income in their NBA career.


# our main menu
end = 1
while end == 1:
    print("Choose the number of your question")
    print("1.What's this year's schedule for _____ team?")
    print("2.How many blocks does _____ player have this season?")
    print("3.What is the roster for ___ team this season?")
    print("4.How many 3-pointers did _____ player make in their NBA career?")
    print("5.How many steals did _____ player achieve in their NBA career?")
    print("6.How many points did _____ player make in their NBA career?")
    print("7.How much did _____ player make in their NBA career?")
    print("10. I'm feeling lucky.")

    # prompted a question
    text = input("")
    # If they press I'm feeling lucky, get the random int
    if text == '10':
        text = get_random_int_from_database()

    if text == '1':
        # input must be the team abbreviation! So GSW for golden state team, etc.
        print("Input team's abbreviation")
        team = input("")
        nba_schedule(team)
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '2':
        player_blocks()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '3':
        # input must be the team abbreviation! So GSW for golden state team, etc.
        print("Input team's abbreviation")
        team = input("")
        nba_roster(team)
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '4':
        player_three_pointers()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '5':
        player_steals()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '6':
        player_points()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
    if text == '7':
        player_salary()
        text = input("Want to exit? press 0. If not, press 1")
        if text == '0':
            end = 0
        else:
            print("\n")
