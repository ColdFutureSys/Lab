stack_items = []

print("=== STACK ===")
print("Multi-item clipboard organizer")

while True:

    print("\n1. Add Item")
    print("2. View Stack")
    print("3. Copy All")
    print("4. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":

        item = input("Enter text: ")

        stack_items.append(item)

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

        print("Goodbye.")
        break

    else:
        print("Invalid option.")
