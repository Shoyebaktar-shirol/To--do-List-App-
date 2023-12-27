import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        self.tasks = []

        self.heading_label = tk.Label(root, text="Todo List", font=("Helvetica", 16, "italic"))
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=20)
        

       
        self.task_entry = tk.Text(root, width=40, height=5) 
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)


        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=100, height=10)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
