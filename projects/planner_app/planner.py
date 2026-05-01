import os
import json

tasks = []

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks():
    print("\n=== TASKS ===")

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    name = input("Task name: ")
    category = input("Category: ")
    priority = input("Priority (HIGH/MEDIUM/LOW): ")
    due_date = input("Due date: ")

    task = f"[TODO][{category}][{priority}] {name} - Due: {due_date}"

    tasks.append(task)

    save_tasks()

    print("Task added.")


def complete_task():
    view_tasks()

    try:
        completed = int(input("Task number to complete: "))

        if 0 < completed <= len(tasks):
            tasks[completed - 1] = tasks[completed - 1].replace(
                "[TODO]",
                "[DONE]"
            )

            save_tasks()

            print("Task completed.")

        else:
            print("Invalid task number.")

    except:
        print("Please enter a number.")


def filter_tasks():
    keyword = input("Filter keyword: ").upper()

    print("\n=== FILTERED TASKS ===")

    found = False

    for task in tasks:
        if keyword in task.upper():
            print(task)
            found = True

    if not found:
        print("No matching tasks.")

def dashboard():
    total = len(tasks)

    completed = 0
    high_priority = 0

    for task in tasks:
        if "[DONE]" in task:
            completed += 1

        if "[HIGH]" in task:
            high_priority += 1

    pending = total - completed

    print("\n=== DASHBOARD ===")
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"High Priority: {high_priority}")

while True:
    print("\n=== COMMAND PLANNER ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Filter Tasks")
    print("5. Dashboard")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        filter_tasks()

    elif choice == "5":
        dashboard()

    elif choice == "6":
        print("Goodbye.")
    break

    else:
        print("Invalid option.")
