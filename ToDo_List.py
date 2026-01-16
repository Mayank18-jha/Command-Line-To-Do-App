import json
import os

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Load tasks
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Enter task title: ")
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "status": "Pending"})
    save_tasks()
    print("Task added")

def view_tasks():
    if not tasks:
        print("📭 No tasks found")
        return
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {task['status']}")

def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks()
            print("🔄 Task updated")
            return
    print("Task not found")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks()
    print("Task deleted")

def menu():
    while True:
        print("""
====== TO-DO APP ======
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
""")
        choice = input("Choose option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Bye!")
            break
        else:
            print("Invalid choice")

menu()
