import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the entry field after adding
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to edit a selected task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()
        selected_task = task_listbox.get(selected_task_index)
        new_task = task_entry.get()
        if new_task != "":
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)  # Clear the entry field after editing
        else:
            messagebox.showwarning("Input Error", "Please enter the new task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the task entry field
task_entry = tk.Entry(root, width=40, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Create the Add Task button
add_button = tk.Button(root, text="Add Task", width=20, font=("Arial", 14), command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Create the listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 14), selectmode=tk.SINGLE)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create the Delete Task button
delete_button = tk.Button(root, text="Delete Task", width=20, font=("Arial", 14), command=delete_task)
delete_button.grid(row=2, column=0, padx=10, pady=10)

# Create the Edit Task button
edit_button = tk.Button(root, text="Edit Task", width=20, font=("Arial", 14), command=edit_task)
edit_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop of the app
root.mainloop()
