import json
import os

PRIORITY_ORDER = {"High": 3, "Medium": 2, "Low": 1}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

tasks = []
if os.path.exists("tasks.json"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []

def show_tasks(tasks):
    print("\n=== TASK LIST ===")

    if not tasks:
        print("No tasks yet.")
        return

    sorted_tasks = sorted(
        tasks,
        key=lambda x: PRIORITY_ORDER.get(x["priority"], 0),
        reverse=True
    )

    for i, task in enumerate(sorted_tasks, start=1):
        status = "✓" if task["done"] else "•"
        print(f"{i}. [{status}] {task['name']} ({task['priority']})")

while True:
    print("\n========================")
    print("   COMMAND PLANNER")
    print("========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Toggle Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        name = input("Task name: ")
        priority = input("Priority (Low/Medium/High): ").capitalize()

        if priority not in ["Low", "Medium", "High"]:
            priority = "Low"

        tasks.append({
            "name": name,
            "priority": priority,
            "done": False
        })

        save_tasks(tasks)
        print("✓ Task added.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)

        try:
            num = int(input("Task number: "))
            tasks[num - 1]["done"] = not tasks[num - 1]["done"]
            save_tasks(tasks)
            print("✓ Updated.")
        except:
            print("Invalid input.")

    elif choice == "4":
        show_tasks(tasks)

        try:
            num = int(input("Task number: "))
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['name']}")
        except:
            print("Invalid input.")

    elif choice == "5":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")
