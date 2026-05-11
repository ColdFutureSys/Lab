import json
import os

FILE = "stack.json"

# Load saved stack
if os.path.exists(FILE):
    with open(FILE, "r") as file:
        stack_items = json.load(file)
else:
    stack_items = []

print("=== STACK ===")
print("Multi-item clipboard organizer")

while True:

    print("\n1. Add Item")
    print("2. View Stack")
    print("3. Copy All")
    print("4. Copy One Item")
    print("5. Delete Item")
    print("6. Clear Stack")
    print("7. Exit")

    choice = input("\nChoose option: ")

    # ADD ITEM
    if choice == "1":

        item = input("Enter text: ")

        stack_items.append(item)

        with open(FILE, "w") as file:
            json.dump(stack_items, file)

        print("Added.")

    # VIEW STACK
    elif choice == "2":

        print("\n=== CURRENT STACK ===")

        if not stack_items:
            print("Stack is empty.")

        else:
            for i, item in enumerate(stack_items, start=1):
                print(f"{i}. {item}")

    # COPY ALL
    elif choice == "3":

        if not stack_items:
            print("Stack is empty.")

        else:
            combined = "\n".join(stack_items)

            print("\n=== COPIED TEXT ===")
            print(combined)

    # COPY ONE ITEM
    elif choice == "4":

        print("\n=== COPY ITEM ===")

        if not stack_items:
            print("Stack is empty.")

        else:
            for i, item in enumerate(stack_items, start=1):
                print(f"{i}. {item}")

            try:
                number = int(input("Item number: "))

                copied = stack_items[number - 1]

                print("\n=== COPIED ITEM ===")
                print(copied)

            except:
                print("Invalid selection.")

    # DELETE ITEM
    elif choice == "5":

        print("\n=== DELETE ITEM ===")

        if not stack_items:
            print("Stack is empty.")

        else:
            for i, item in enumerate(stack_items, start=1):
                print(f"{i}. {item}")

            try:
                number = int(input("Item number to delete: "))

                removed = stack_items.pop(number - 1)

                with open(FILE, "w") as file:
                    json.dump(stack_items, file)

                print(f"Deleted: {removed}")

            except:
                print("Invalid selection.")

    # CLEAR STACK
    elif choice == "6":

        stack_items.clear()

        with open(FILE, "w") as file:
            json.dump(stack_items, file)

        print("Stack cleared.")

    # EXIT
    elif choice == "7":

        print("Goodbye.")
        break

    else:
        print("Invalid option.")
