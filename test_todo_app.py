#!/usr/bin/env python3
"""
Test script for the To-Do List application
Tests basic functionality and imports
"""

import sys
import tkinter as tk
from todo_app import TodoApp

def test_app():
    """Test the To-Do App basic functionality"""
    print("Testing To-Do List Application...")
    
    # Test 1: Import
    print("✓ Successfully imported TodoApp")
    
    # Test 2: Create root window
    root = tk.Tk()
    root.withdraw()  # Hide the window
    print("✓ Successfully created Tk root window")
    
    # Test 3: Initialize app
    app = TodoApp(root)
    print("✓ Successfully initialized TodoApp")
    
    # Test 4: Add a task programmatically
    app.task_entry.insert(0, "Test Task 1")
    app.add_task()
    assert app.task_listbox.size() == 1, "Failed to add task"
    print("✓ Successfully added a task")
    
    # Test 5: Add another task
    app.task_entry.insert(0, "Test Task 2")
    app.add_task()
    assert app.task_listbox.size() == 2, "Failed to add second task"
    print("✓ Successfully added second task")
    
    # Test 6: Mark task as complete
    app.task_listbox.selection_set(0)
    app.mark_complete()
    task = app.task_listbox.get(0)
    assert task.startswith("✓ "), "Failed to mark task as complete"
    print("✓ Successfully marked task as complete")
    
    # Test 7: Delete a task
    app.task_listbox.selection_set(1)
    app.delete_task()
    assert app.task_listbox.size() == 1, "Failed to delete task"
    print("✓ Successfully deleted a task")
    
    # Test 8: Counter update
    counter_text = app.counter_label.cget("text")
    assert "1" in counter_text, "Counter not updated correctly"
    print("✓ Task counter working correctly")
    
    # Clean up
    root.destroy()
    print("\n✓ All tests passed!")
    print("The To-Do List application is working correctly!")
    
    return True

if __name__ == "__main__":
    try:
        test_app()
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
