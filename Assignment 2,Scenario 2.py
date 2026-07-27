# Cricket Team Management System

class Player:
    def __init__(self, name, jersey, runs):
        self.name = name
        self.jersey = jersey
        self.runs = runs

    def category(self):
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 200:
            return "Good"
        else:
            return "Average"


class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter Player Name: ")
        jersey = int(input("Enter Jersey Number: "))
        runs = int(input("Enter Runs: "))

        player = Player(name, jersey, runs)
        self.players.append(player)

        print("Player Added Successfully!")

    def show_players(self):
        if len(self.players) == 0:
            print("No Players Found.")
        else:
            print("\nPlayer Details")
            print("----------------------------")
            for p in self.players:
                print("Name :", p.name)
                print("Jersey Number :", p.jersey)
                print("Runs :", p.runs)
                print("Category :", p.category())
                print("----------------------------")


team = Team()

while True:
    print("\n Cricket Team Management ")
    print("1. Add Player")
    print("2. Show Players")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        team.add_player()

    elif choice == "2":
        team.show_players()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
Comment:-
Cricket Team Management 
1. Add Player
2. Show Players
3. Exit
Enter Choice: 1

Enter Player Name: Rohit Sharma
Enter Jersey Number: 45
Enter Runs: 650
Player Added Successfully!

 Cricket Team Management 
1. Add Player
2. Show Players
3. Exit
Enter Choice: 2

Player Details
Name : Rohit Sharma
Jersey Number : 45
Runs : 650
Category : Excellent
