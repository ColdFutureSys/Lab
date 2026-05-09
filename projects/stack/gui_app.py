import tkinter as tk
from tkinter import messagebox

stack_items = []

# ---------- FUNCTIONS ----------

def refresh_list():

    listbox.delete(0, tk.END)

    for item in stack_items:
        listbox.insert(tk.END, item)

def add_item():

    text = entry.get()

    if not text:
        messagebox.showwarning(
            "Error",
            "Enter some text."
        )
        return

    stack_items.append(text)

    entry.delete(0, tk.END)

    refresh_list()

def copy_all():

    combined = "\n".join(stack_items)

    output_label.config(
        text=combined
    )

def delete_item():

    try:
        index = listbox.curselection()[0]

        stack_items.pop(index)

        refresh_list()

    except:
        messagebox.showwarning(
            "Error",
            "Select an item."
        )

# ---------- WINDOW ----------

root = tk.Tk()

root.title("Stack")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

# ---------- INPUT ----------

entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14)
)

entry.pack(pady=10)

# ---------- BUTTONS ----------

tk.Button(
    root,
    text="Add Item",
    command=add_item,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

tk.Button(
    root,
    text="Copy All",
    command=copy_all,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

tk.Button(
    root,
    text="Delete Selected",
    command=delete_item,
    bg="#333333",
    fg="white",
    width=20,
    font=("Arial", 12)
).pack(pady=5)

# ---------- LIST ----------

listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    bg="#2b2b2b",
    fg="white",
    font=("Consolas", 12)
)

listbox.pack(pady=15)

# ---------- OUTPUT ----------

output_label = tk.Label(
    root,
    text="",
    bg="#1e1e1e",
    fg="white",
    justify="left",
    font=("Arial", 11)
)

output_label.pack(pady=10)

root.mainloop()
