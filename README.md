# To-Do List Manager (Simple Version)

## Group Members
- Amir Hossein Najafi (301497935)
- Bron Banks (301391190)
- Vaancha Pandey (301540239)

## Project Title
To-Do List Manager (Simple Version)

## Description
This Python program allows users to manage a simple to-do list. 
Users can:
- Add tasks
- View tasks
- Remove tasks

Tasks are stored in a plain text file (`tasks.txt`). The program demonstrates basic Python programming, file handling, and input validation.

## Instructions to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/vaancha/python-assignment.git
2. Navigate to project folder:
   ```bash
   cd python-assignment
3. Run the program:
   ```bash
   python todo.py

SAMPLE OUTPUT
pc@LAPTOP-V38R86V8 MINGW64 /c/users/pc/downloads/lab assignment 3 comp 120 (main)
$ python todo.py

To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 1
No tasks found. Your to-do list is empty.

To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 2
Enter the task to add: eat breakfast
Task added: eat breakfast

To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 2
Enter the task to add: go to classes
Task added: go to classes

To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 1

Your Tasks:
1. eat breakfast
2. go to classes


To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 3

Your Tasks:
1. eat breakfast
2. go to classes

Enter the task number to remove: 1
Removed task: eat breakfast

To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 1

Your Tasks:
1. go to classes


To-Do List Manager - Simple Version
----------------------------------
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 4
Goodbye — your tasks have been saved.

pc@LAPTOP-V38R86V8 MINGW64 /c/users/pc/downloads/lab assignment 3 comp 120 (main)
$

## Git Logs and Repository Status

### Commit History
pc@LAPTOP-V38R86V8 MINGW64 /c/users/pc/downloads/lab assignment 3 comp 120 (main)
$ git log --oneline
b359f0e (HEAD -> main, origin/main) Merge pull request #1 from vaancha/feature-update
08e88af Implement task length validation in add_task
0353caf Add sample output to README for To-Do List Manager
a2df139 Update README with project information and instructions
5637a7e add task description comment
a575dd9 add header comment to todo.py
c8b8cf4 add task description comment
9fb8643 add header comment to todo.py
697eb51 Add common files to .gitignore
3643e02 Add files via upload
0717224 Initial commit


### Branches
pc@LAPTOP-V38R86V8 MINGW64 /c/users/pc/downloads/lab assignment 3 comp 120 (main)
$ git branch
* main


### Repository Status
pc@LAPTOP-V38R86V8 MINGW64 /c/users/pc/downloads/lab assignment 3 comp 120 (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean




