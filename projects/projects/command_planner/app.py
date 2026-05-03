tasks = []

while True:
    print("\n--- COMMAND PLANNER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nTASKS:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
