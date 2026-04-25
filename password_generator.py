import random

words = [
    "shadow",
    "tiger",
    "rocket",
    "matrix",
    "ghost",
    "falcon",
    "vortex",
    "neon"
]

while True:

    print("\n=== Password Generator ===")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        chosen_word = random.choice(words)

        number = random.randint(100, 999)

        symbol = random.choice(["!", "@", "#", "$"])

        password = chosen_word + str(number) + symbol

        print("\nGenerated Password:")
        print(password)

    elif choice == "2":

        print("Program closed.")

        break

    else:

        print("Invalid option.")
