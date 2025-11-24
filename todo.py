"""
To-Do List Manager (Simple Version)
- Add tasks
- View tasks
- Remove tasks
- Tasks are stored in a plain text file (tasks.txt)

Authors: Amir Hossein Najafi (301497935)
         Bron Banks (301391190)
         Vaancha Pandey (301540239)
"""

import os
from typing import List

TASKS_FILE = "tasks.txt"


def load_tasks(filename: str = TASKS_FILE) -> List[str]:
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            # Strip newline and ignore empty lines
            tasks = [line.strip() for line in f if line.strip()]
    return tasks


def save_tasks(tasks: List[str], filename: str = TASKS_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(tasks: List[str], task: str) -> None:
    task = task.strip()
    if not task:
        print("Cannot add an empty task.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")


def view_tasks(tasks: List[str]) -> None:
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print("")  # blank line


def remove_task(tasks: List[str], index: int) -> None:
    if index < 1 or index > len(tasks):
        print("Invalid task number. No task removed.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Removed task: {removed}")


def print_menu() -> None:
    menu = """
To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit
"""
    print(menu)


def main() -> None:
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task to add: ").strip()
            add_task(tasks, task)
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            view_tasks(tasks)
            idx_str = input("Enter the task number to remove: ").strip()
            if not idx_str.isdigit():
                print("Please enter a valid number.")
                continue
            remove_task(tasks, int(idx_str))
        elif choice == "4":
            print("Goodbye — your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
