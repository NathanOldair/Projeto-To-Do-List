from models.user import User
from models.task import Task
from models.category import Category
from utils.authentication import Authentication

def main():
    print("Welcome to the To-Do List Manager")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                user = Authentication.register(username, password)
                print(f"User {username} registered successfully.")
            except Exception as e:
                print(e)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                user = Authentication.login(username, password)
                print(f"User {username} logged in successfully.")
                user_menu(user)
            except Exception as e:
                print(e)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

def user_menu(user):
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (Low/Medium/High): ")
            category_name = input("Enter task category: ")
            category = Category(category_name)
            task = Task(title, description, due_date, priority, category)
            user.add_task(task)
            print(f"Task '{title}' added successfully.")
        
        elif choice == '2':
            tasks = user.get_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")
        
        elif choice == '3':
            task_title = input("Enter task title to remove: ")
            task_to_remove = None
            for task in user.get_tasks():
                if task.title == task_title:
                    task_to_remove = task
                    break
            if task_to_remove:
                user.remove_task(task_to_remove)
                print(f"Task '{task_title}' removed successfully.")
            else:
                print("Task not found.")
        
        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()