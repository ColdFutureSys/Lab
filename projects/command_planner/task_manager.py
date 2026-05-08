import json
import os

FILE = "tasks.json"

PRIORITY_ORDER = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}


FILE = "tasks.json"

PRIORITY_ORDER = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, name, priority):
    tasks.append({
        "name": name,
        "priority": priority,
        "done": False
    })

    save_tasks(tasks)

def toggle_task(tasks, index):
    tasks[index]["done"] = not tasks[index]["done"]
    save_tasks(tasks)

def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

def sorted_tasks(tasks):
    return sorted(
        tasks,
        key=lambda x: PRIORITY_ORDER.get(x["priority"], 0),
        reverse=True
    )
