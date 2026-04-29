import os

tasks = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()

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
priority = input("Priority (HIGH/MEDIUM/LOW): ")
due_date = input("Due date: ")
full_task = f"[{priority}] {new_task} - Due: {due_date}"
        tasks.append(full_task)

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")
        
        print("Task added.")

 elif choice == "3":
    completed = input("Task to complete: ")

    if completed in tasks:
        tasks[completed - 1] = "[DONE] " + tasks[completed - 1]

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("Task completed.")
    else:
        print("Task not found.")

elif choice == "4":
    print("Goodbye.")
    break 
