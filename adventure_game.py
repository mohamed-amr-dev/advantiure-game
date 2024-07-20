import time
import random

# List of monsters
monsters = ("dragon", "pirate", "witch", "griffin")
monster = random.choice(monsters)

# Print_pause function to pause output for 2 seconds


def print_pause(message):
    print(message)
    time.sleep(2)


# Player name
name = input("Name: ").capitalize()
print_pause(f"Hello {name}")

score = 1

# Functions to modify score


def increase_score():
    global score
    score += 2


def decrease_score():
    global score
    score -= 1


def keep_score():
    global score
    score += 0

# Ask player if they're ready to start


def ask():
    while True:
        ready = input("Are you ready for adventure? (yes/no): ").lower()
        if ready == "yes":
            print_pause("Let's go!")
            break
        elif ready == "no":
            print_pause("Have fun, bye!")
            exit()
        else:
            print_pause("Please enter 'yes' or 'no'.")

# Game introduction


def intro():
    print_pause("You were camping with your friends on a mission.")
    print_pause(f"The mission is to kill the {monster}.")
    print_pause(f"You got lost, {name}.")
    print_pause("What will you do?")
    print_pause("1. Stay in your place.")
    print_pause("2. Trust in yourself and walk alone.")

    while True:
        first_choice = input("Enter (1/2): ")
        if first_choice == "1":
            keep_score()
            print_pause(f"You waited a long time, {name}.")
            print_pause("And the next day comes.")
            print_pause("You need to move now.")
            forest()
            forest_choice()
            break
        elif first_choice == "2":
            keep_score()
            forest()
            forest_choice()
            break
        else:
            print_pause("Please enter 1 or 2.")

# Forest scenario


def forest():
    print_pause("You walk a lot in the forest.")
    print_pause("And now it's sunset time.")
    print_pause("You find a cave and a house.")
    print_pause("What will you do?")

# Forest choice


def forest_choice():
    print_pause("1. Enter the cave.")
    print_pause("2. Knock on the door of the house.")

    while True:
        choice = input("Enter (1/2): ")
        if choice == "1":
            increase_score()
            cave()
            break
        elif choice == "2":
            house()
            break
        else:
            print_pause("Please enter 1 or 2.")

# Cave scenario


def cave():
    print_pause("You entered the cave.")
    print_pause("It was a small cave.")
    print_pause("You see a magical wand.")
    print_pause("You take the wand.")
    end()

# House scenario


def house():
    print_pause("You were about to knock on the door.")
    print_pause(f"When the door opens and out steps a {monster}.")
    print_pause(f"This is the {monster}'s house!")
    print_pause(f"The {monster} finds you!")
    print_pause("You feel a bit under-prepared for this,")
    print_pause("what with only having a tiny, rusty old magic wand.")

    while True:
        choice = input(
            "Would you like to (1) cast a spell or (2) run away? Enter (1/2): ")
        if choice == "1":
            print_pause("You do your best...")
            print_pause("But your rusty old magic wand is too weak.")
            print_pause(f"You can't defeat the {monster}.")
            print_pause("You have been turned into a frog!")
            decrease_score()
            game_loop()
            break
        elif choice == "2":
            print_pause("Now there's no way except the cave.")
            increase_score()
            cave()
            break
        else:
            print_pause("Please enter 1 or 2.")

# End of game


def end():
    print_pause(f"Now you will go to the {monster}'s house.")
    print_pause(f"As the {monster} moves to cast a spell,")
    print_pause("you raise your new wand.")
    print_pause("The wand shines brightly in your hand.")
    print_pause("You brace yourself for the spell.")
    print_pause(f"But the {monster} takes one look")
    print_pause("At your shiny new wand and runs away!")
    print_pause(f"You have rid the town of the {monster}.")
    print_pause("You are victorious! 🤩")
    game_loop()

# Main game loop


def game_loop():
    print_pause(f"Your score is {score}")
    while True:
        again = input("Would you like to play again? (yes/no): ")
        if again == "yes":
            game()
            break
        elif again == "no":
            print("Goodbye!")
            exit()
        else:
            print_pause("Please enter 'yes' or 'no'.")

# Main function to start the game


def game():
    global score
    score = 1
    ask()
    intro()


game()
