import tkinter as tk
from tkinter import ttk

priority_colors = {"High": "red", "Medium": "orange", "Low": "green"}
priority_order = {"High": 0, "Medium": 1, "Low": 2}

tasks = []

def save_task():
    task_text = entry.get().strip()
    priority = priority_var.get()
    if task_text:
        tasks.append({"task": task_text, "priority": priority})
        entry.delete(0, tk.END)
        update_display()

def delete_task(index):
    del tasks[index]
    update_display()

def update_display():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    tasks.sort(key=lambda x: priority_order[x["priority"]])

    for i, task in enumerate(tasks):
        task_text = f"{task['task']} ({task['priority']})"
        color = priority_colors[task["priority"]]

        label = tk.Label(task_list_frame, text=task_text, fg=color, font=("Arial", 11), anchor="w")
        label.grid(row=i, column=0, sticky="w", padx=10, pady=2)

        del_btn = tk.Button(task_list_frame, text="Delete", font=("Arial", 9), command=lambda i=i: delete_task(i))
        del_btn.grid(row=i, column=1, padx=5, pady=2)

root = tk.Tk()
root.title("Smart To-Do List")
root.geometry("430x500")
root.resizable(False, False)

event_label = tk.Label(root, text="Event:", font=("Arial", 11))
event_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")

priority_label = tk.Label(root, text="Priority:", font=("Arial", 11))
priority_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

priority_var = tk.StringVar(value="Medium")
priority_menu = ttk.OptionMenu(root, priority_var, "Medium", "High", "Medium", "Low")
priority_menu.grid(row=1, column=1, padx=10, pady=5, sticky="w")

save_btn = tk.Button(root, text="Add Task", command=save_task, font=("Arial", 11))
save_btn.grid(row=2, column=0, columnspan=2, pady=10)

task_list_frame = tk.Frame(root)
task_list_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

root.mainloop()
