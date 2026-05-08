import tkinter as tk
from tkinter import messagebox

from task_manager import (
    load_tasks,
    add_task,
    toggle_task,
    delete_task,
    sorted_tasks
)

tasks = load_tasks()

# ---------- FUNCTIONS ----------

def refresh_list():
    listbox.delete(0, tk.END)

    for task in sorted_tasks(tasks):
        status = "✓" if task["done"] else "•"

        text = (
            f"[{status}] "
            f"{task['name']} "
            f"({task['priority']})"
        )

        listbox.insert(tk.END, text)

def add_task_gui():
    name = entry.get()
    priority = priority_var.get()

    if not name:
        messagebox.showwarning(
            "Error",
            "Please enter a task."
        )
        return

    add_task(tasks, name, priority)

    entry.delete(0, tk.END)

    refresh_list()

def toggle_task_gui():
    try:
        index = listbox.curselection()[0]

        toggle_task(tasks, index)

        refresh_list()

    except:
        messagebox.showwarning(
            "Error",
            "Select a task."
        )

def delete_task_gui():
    try:
        index = listbox.curselection()[0]

        delete_task(tasks, index)

        refresh_list()

    except:
        messagebox.showwarning(
            "Error",
            "Select a task."
        )

# ---------- WINDOW ----------

root = tk.Tk()

root.title("Command Planner")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

# ---------- INPUT ----------

entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14)
)

entry.pack(pady=10)

# ---------- PRIORITY ----------

priority_var = tk.StringVar(value="Low")

priority_menu = tk.OptionMenu(
    root,
    priority_var,
    "Low",
    "Medium",
    "High"
)

priority_menu.pack(pady=5)

# ---------- BUTTONS ----------

tk.Button(
    root,
    text="Add Task",
    command=add_task_gui,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

tk.Button(
    root,
    text="Toggle Complete",
    command=toggle_task_gui,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

tk.Button(
    root,
    text="Delete Task",
    command=delete_task_gui,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

# ---------- TASK LIST ----------

listbox = tk.Listbox(
    root,
    width=50,
    height=15,
    bg="#2b2b2b",
    fg="white",
    font=("Consolas", 12)
)

listbox.pack(pady=15)

refresh_list()

root.mainloop()
