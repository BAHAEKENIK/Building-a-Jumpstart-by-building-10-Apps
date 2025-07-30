def main():
    greeting()
    persone = get_name()
    nice_meeting(persone)


def greeting():
    print("------------------------------------------")
    print("                 Hello APP                ")
    print("------------------------------------------")


def get_name():
    name = input("What is your name ? ")
    return name


def nice_meeting(name):
    print(f"Nice to meet you {name}")


if __name__ == "__main__":
    main()
