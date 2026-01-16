# Simple To-Do List Application

A simple and user-friendly GUI-based to-do list manager built with Python and tkinter.

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list
- **Mark as Complete**: Mark tasks as completed with a checkmark (✓)
- **Delete Tasks**: Remove individual tasks from your list
- **Clear All**: Clear all tasks at once with a confirmation dialog
- **Task Counter**: See the total number of tasks in your list
- **Keyboard Support**: Press Enter to add tasks quickly

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## Installation

1. Make sure you have Python 3 installed on your system:
   ```bash
   python3 --version
   ```

2. On Ubuntu/Debian, if tkinter is not installed:
   ```bash
   sudo apt install python3-tk
   ```

3. Clone or download this repository

## Usage

Run the application using:

```bash
python3 todo_app.py
```

Or make it executable and run directly:

```bash
chmod +x todo_app.py
./todo_app.py
```

## How to Use

1. **Adding a Task**: Type your task in the text field and click "Add Task" or press Enter
2. **Marking Complete**: Select a task from the list and click "Mark Complete"
3. **Deleting a Task**: Select a task from the list and click "Delete Task"
4. **Clearing All Tasks**: Click "Clear All" to remove all tasks (requires confirmation)

## Application Layout

- **Title**: "My To-Do List" at the top
- **Input Field**: Enter new tasks here
- **Add Task Button**: Add the task to your list
- **Task List**: Displays all your tasks with scrollbar support
- **Action Buttons**: 
  - Mark Complete (blue)
  - Delete Task (red)
  - Clear All (orange)
- **Task Counter**: Shows the total number of tasks

## Screenshots

The application features a clean, modern interface with:
- Color-coded buttons for different actions
- A scrollable list for managing multiple tasks
- Visual feedback when tasks are completed (checkmark and gray text)

## License

MIT License - Feel free to use and modify as needed.
