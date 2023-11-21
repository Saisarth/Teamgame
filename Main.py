import time

class TextAdventureGame:
    def __init__(self):
        self.player_name = ""
        self.player_inventory = []
        self.current_location = "Entrance"

    def introduction(self):
        print("Welcome to the Text-Based Adventure Game!")
        self.player_name = input("Enter your name: ")
        time.sleep(1)
        print(f"{self.player_name}, you find yourself at the entrance of a mysterious cave.")

    def make_choice(self, choices):
        print("\nChoose your action:")
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(choices):
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def explore_cave(self):
        print(f"\n{self.player_name}, you decide to explore the cave.")
        time.sleep(1)
        print("You encounter a fork in the path.")

        choices_fork = ["Go left", "Go right"]
        choice_fork = self.make_choice(choices_fork)

        if choice_fork == 1:
            print("You discover a hidden treasure!")
            self.player_inventory.append("Treasure")
        else:
            print("A giant spider blocks your way. Game over!")

    def play_game(self):
        self.introduction()

        choices_entrance = ["Enter the cave", "Turn back"]
        choice_entrance = self.make_choice(choices_entrance)

        if choice_entrance == 1:
            self.explore_cave()
        else:
            print(f"\n{self.player_name}, you decide not to enter the cave. The adventure ends.")

if __name__ == "__main__":
    game = TextAdventureGame()
    game.play_game()
