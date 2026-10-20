# To-Do List Application

A simple command-line task management application built with Python using Object-Oriented Programming (OOP) and JSON file storage. It allows users to organize tasks and track their completion status.

## Features

- **Add Tasks:** Create new tasks with a title.
- **View Tasks:** Display all tasks with their completion status.
- **Complete Tasks:** Mark tasks as completed.
- **Delete Tasks:** Remove tasks from the list.
- **Persistent Storage:** Save tasks in a JSON file so they remain available after restarting the application.
- **Input Validation:** Handle empty task titles, invalid menu choices, and incorrect task numbers.
- **Exception Handling:** Handle invalid JSON data and certain file permission errors.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling

## Project Structure

```text
To-Do-List/
├── todo.py
├── tasks.json
└── README.md
```

- `todo.py` — Contains the application logic and menu.
- `tasks.json` — Stores task data in JSON format and is created when tasks are saved.
- `README.md` — Project documentation.

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- No external Python packages are required.

### Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd To-Do-List
   ```

3. Run the application:

   ```bash
   python todo.py
   ```

## Usage

After running the program, choose an option from the menu:

```text
1. View
2. Add
3. Complete
4. Delete
5. Exit
```

Enter the corresponding number to perform an operation.

### Example Output

```text
--Your Tasks--
1. [ ] Complete Python project
2. [X] Practice programming
--------------------
```

`[ ]` indicates an incomplete task, while `[X]` indicates a completed task.

## Concepts Practiced

- Classes, objects, constructors, and methods
- Lists and dictionaries
- Loops and conditional statements
- JSON serialization and deserialization
- File handling
- Exception handling
- Input validation
- Persistent data storage

## Future Improvements

- Add task priorities.
- Add due dates and reminders.
- Implement task editing.
- Filter tasks by completion status.
- Add a graphical user interface (GUI).
- Display task completion statistics.

## Author

**Mitesh Rk**

GitHub: https://github.com/miteshrk981-oss

---

*This project was developed to practice Python programming, OOP, and file-based data persistence.*
