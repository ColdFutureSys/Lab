tasks = []

while True:
    print("\n=== PLANNER ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("\nTasks:")
        for task in tasks:
            print("-", task)

    elif choice == "2":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task added.")

 elif choice == "3":
    completed = input("Task to complete: ")

    if completed in tasks:
        tasks.remove(completed)
        print("Task completed.")
    else:
        print("Task not found.")

elif choice == "4":
    print("Goodbye.")
    break 
