
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("You're at a crossroad. Where do you want to go?")
choice1 = input("Type 'left' or 'right': ").lower()

if choice1 == "left":
    print("You arrive at a lake.")
    choice2 = input("Do you want to 'swim' or 'wait' for a boat? ").lower()

    if choice2 == "wait":
        print("A boat arrives and takes you to an island.")
        choice3 = input(
            "You see three doors: 'red', 'blue', and 'yellow'. "
        ).lower()

        if choice3 == "yellow":
            print("You found the treasure!")
            print("Congratulations! YOU WIN! 🏆")
        elif choice3 == "red":
            print("The room is full of fire. Game over! 🔥")
        elif choice3 == "blue":
            print("You enter a room full of hungry beasts. Game over! 🐉")
        else:
            print("That door doesn't exist. Game over!")

    else:
        print("You were attacked by a crocodile. Game over! 🐊")

else:
    print("You fell into a hole. Game over! 💀")
