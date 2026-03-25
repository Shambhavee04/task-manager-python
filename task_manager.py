import json

FILE = "tasks.json"

# Load tasks
def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})

# View tasks
def view_tasks(tasks):
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

# Mark done
def mark_done(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number: "))
    tasks[num-1]["done"] = True

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number: "))
    tasks.pop(num-1)

# Main loop
tasks = load_tasks()

while True:
    print("\n1.Add 2.View 3.Done 4.Delete 5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        save_tasks(tasks)
        break