
tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    display_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    if task_number >= 0 and task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted!")
    else:
        print("Invalid task number!")

while True:
    print("\n1. Display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
