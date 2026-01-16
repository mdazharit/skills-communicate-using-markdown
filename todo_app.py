#!/usr/bin/env python3
"""
Simple To-Do List Application
A GUI-based to-do list manager using Python tkinter
"""

import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        """Initialize the To-Do List application"""
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        # Configure colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.delete_color = "#f44336"
        
        self.root.configure(bg=self.bg_color)
        
        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Label
        title_label = tk.Label(
            self.root,
            text="My To-Do List",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Frame for entry and add button
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)
        
        # Entry field for new tasks
        self.task_entry = tk.Entry(
            input_frame,
            width=30,
            font=("Arial", 12)
        )
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        # Add button
        add_button = tk.Button(
            input_frame,
            text="Add Task",
            command=self.add_task,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            width=10
        )
        add_button.pack(side=tk.LEFT, padx=5)
        
        # Frame for listbox and scrollbar
        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(
            list_frame,
            width=45,
            height=15,
            font=("Arial", 11),
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            selectbackground="#4CAF50"
        )
        self.task_listbox.pack(side=tk.LEFT)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Frame for action buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        # Complete button
        complete_button = tk.Button(
            button_frame,
            text="Mark Complete",
            command=self.mark_complete,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            width=15
        )
        complete_button.pack(side=tk.LEFT, padx=5)
        
        # Delete button
        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task,
            bg=self.delete_color,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            width=15
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        # Clear all button
        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_all,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            width=15
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Task counter label
        self.counter_label = tk.Label(
            self.root,
            text="Total Tasks: 0",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#666"
        )
        self.counter_label.pack(pady=10)
        
    def add_task(self):
        """Add a new task to the list"""
        task = self.task_entry.get().strip()
        
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.update_counter()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
            
    def delete_task(self):
        """Delete the selected task"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.update_counter()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            
    def mark_complete(self):
        """Mark the selected task as complete"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            
            # Check if already marked as complete
            if not task.startswith("✓ "):
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, "✓ " + task)
                self.task_listbox.itemconfig(selected_index, fg="gray")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
            
    def clear_all(self):
        """Clear all tasks from the list"""
        if self.task_listbox.size() > 0:
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
            if confirm:
                self.task_listbox.delete(0, tk.END)
                self.update_counter()
        else:
            messagebox.showinfo("Info", "The task list is already empty!")
            
    def update_counter(self):
        """Update the task counter label"""
        total_tasks = self.task_listbox.size()
        self.counter_label.config(text=f"Total Tasks: {total_tasks}")


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
