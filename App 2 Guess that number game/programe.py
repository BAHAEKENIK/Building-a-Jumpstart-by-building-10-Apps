from random import randint


def main():
    header()
    player, computer = get_numbers()
    while player != computer:
        if player < computer:
            print(f"Sorry but {player} is LOWER than the number")
        else:
            print(f"Sorry but {player} is HIGHER than the number")
        player = int(input("Guess a number between 0 and 100:"))
    print(f"YES! You've got it. The number was {computer}")


def header():
    print("----------------------------------------------------")
    print("               GUESS THE NUMBER APP                 ")
    print("----------------------------------------------------")


def get_numbers():
    request = int(input("Guess a number between 0 and 100:"))
    computer = randint(1, 100)
    return request, computer


if __name__ == "__main__":
    main()
