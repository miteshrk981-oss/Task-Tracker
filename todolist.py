import json
import os


class Todolist:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return data if isinstance(data, list) else []
            except (json.JSONDecodeError, PermissionError):
                print("Error reading the storage file. Starting fresh.")
                return []
        return []

    def save_tasks(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except PermissionError:
            print("Permission denied: Could not save tasks.")

    def add_task(self, title):
        if not title:
            print("Task cannot be empty.")
            return
        self.tasks.append({"title": title, "completed": False})
        self.save_tasks()
        print("Task added.")

    def list_task(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return

        print("\n--Your Tasks--")
        for index, task in enumerate(self.tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{index}. {status} {task['title']}")
        print("--------------------")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            return True
        return False

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks.pop(index - 1)
            self.save_tasks()
            return True
        return False


def main():
    todo = Todolist()
    while True:
        print("\n1. View\n2. Add\n3. Complete\n4. Delete\n5. Exit")
        ch = input("Option: ").strip()

        if ch == "1":
            todo.list_task()
        elif ch == "2":
            todo.add_task(input("Task: ").strip())
        elif ch == "3":
            todo.list_task()
            try:
                if todo.complete_task(int(input("Task #: "))):
                    print("Task marked as complete.")
                else:
                    print("No task with that number.")
            except ValueError:
                print("Please enter a valid number.")
        elif ch == "4":
            todo.list_task()
            try:
                if todo.delete_task(int(input("Task #: "))):
                    print("Task deleted.")
                else:
                    print("No task with that number.")
            except ValueError:
                print("Please enter a valid number.")
        elif ch == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1 to 5.")


if __name__ == "__main__":
    main()
