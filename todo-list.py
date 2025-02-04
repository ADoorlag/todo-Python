# mark tasks as incomplete
# delete tasks

import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Error saving tasks")

def view_tasks(tasks):
    print("")
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_task(tasks_dict):
    description = input("Enter task description: ").strip()
    if description:
        tasks_dict["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks_dict)
        print("Task created successfully.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to mark as complete: ").strip())
        if task_number > 0 and task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def main():
    save_tasks({"tasks": [{"description": "saved task", "complete": False}]})
    tasks = load_tasks()
    print(tasks)
    
    while True:
        print("\n To-Do List Manager")
        print("1. View tasks")
        print("2. Create task")
        print("3. complete task")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")
            
main()