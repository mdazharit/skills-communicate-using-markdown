#!/usr/bin/env python3
"""
Script to take a screenshot of the To-Do List application
"""

import tkinter as tk
import time
import subprocess
from todo_app import TodoApp

def take_screenshot():
    """Create app, populate with sample data, and take screenshot"""
    # Create root window
    root = tk.Tk()
    app = TodoApp(root)
    
    # Add sample tasks
    sample_tasks = [
        "Buy groceries",
        "Complete Python project",
        "Read a book",
        "Exercise for 30 minutes",
        "Call Mom",
        "Finish homework"
    ]
    
    for task in sample_tasks:
        app.task_entry.insert(0, task)
        app.add_task()
    
    # Mark one task as complete
    app.task_listbox.selection_set(1)
    app.mark_complete()
    
    # Update the window
    root.update()
    
    # Wait a moment for rendering
    time.sleep(0.5)
    
    # Take screenshot using import command
    try:
        subprocess.run(['import', '-window', 'root', 'todo_app_screenshot.png'], check=True)
        print("Screenshot saved as: todo_app_screenshot.png")
    except Exception as e:
        print(f"Screenshot failed: {e}")
    
    # Keep window open for a moment
    time.sleep(1)
    
    # Close
    root.destroy()

if __name__ == "__main__":
    take_screenshot()
