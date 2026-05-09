import json
import os
FILE = "stack.json"
if os.path.exists(FILE):

    with open(FILE, "r") as file:
        stack_items = json.load(file)

else:
    stack_items = []

def save_stack():

    with open(FILE, "w") as file:
        json.dump(stack_items, file, indent=2)

print("=== STACK ===")
print("Multi-item clipboard organizer")

while True:

    print("\n1. Add Item")
    print("2. View Stack")
    print("3. Copy All")
    print("4. Clear Stack")
    print("5. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":

        item = input("Enter text: ")

        stack_items.append(item)
        save_stack()

        print("Added.")

    elif choice == "2":

        print("\n=== CURRENT STACK ===")

        if not stack_items:
            print("Stack is empty.")

        else:
            for i, item in enumerate(stack_items, start=1):
                print(f"{i}. {item}")

    elif choice == "3":

        combined = "\n".join(stack_items)

        print("\n=== COPIED TEXT ===")
        print(combined)

    elif choice == "4":

        stack_items.clear()
        save_stack()

        print("Stack cleared.")

    elif choice == "5":

        print("Goodbye.")
        break

        else:
        print("Invalid option.")
