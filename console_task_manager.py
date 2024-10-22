from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['task_manager_db']
tasks_collection = db['tasks']

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks_collection.insert_one({"title": title, "description": description})
    print("Task added successfully!")

def view_tasks():
    tasks = list(tasks_collection.find())
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Title: {task['title']}, Description: {task['description']}")
    else:
        print("No tasks available.")

def update_task():
    tasks = list(tasks_collection.find())
    if tasks:
        view_tasks()
        task_index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_title = input("Enter new title (Press Enter to skip): ")
            new_description = input("Enter new description (Press Enter to skip): ")
            update_data = {}
            if new_title:
                update_data["title"] = new_title
            if new_description:
                update_data["description"] = new_description
            if update_data:
                tasks_collection.update_one({"_id": tasks[task_index]["_id"]}, {"$set": update_data})
                print("Task updated successfully!")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available.")

def delete_task():
    tasks = list(tasks_collection.find())
    if tasks:
        view_tasks()
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks_collection.delete_one({"_id": tasks[task_index]["_id"]})
            print(f"Task '{tasks[task_index]['title']}' deleted successfully!")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available.")

while True:
    print("\nInteractive Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Select an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
