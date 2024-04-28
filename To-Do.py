def display_menu():
    print("==== To-Do List Application ====")
    print("1. Add Task")
    print("2. Veiw Tasks")
    print("3. Mark Task as Completed")
    print("4. Edit Tasks")
    print("5. Delete Task")
    print("6. Quit")
    print("================================")

def add_task(todo_list):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (optional): ")

    task = {"Task Name": task_name, "Due Date": due_date, "Priority": priority, "completed": False}
    todo_list.append(task)
    print("Task assed successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the To-Do list.")
    else:
        print("==== Tasks ====") 
        for index, task in enumerate(todo_list, start=1):
            completed_status = "Completed" if task.get("Completed") else "Not Completed"
            print(f"{index}. Task Name: {task['Task Name']}")
            print(f"   Due Date: {task['Due Date']}")
            print(f"   Priority: {task['Priority']}")
            print(f"   Status: {completed_status}")
        print("===============")

def mark_task_completed(todo_list):
    view_tasks(todo_list)

    if not todo_list:
        print("No tasks in the To-Do list.")
        return

    try:
        index = int(input("Enter the index of the task you want to mark as completed: "))
        if 1 <= index <= len(todo_list):
            todo_list[index - 1]["Completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid index. Please enter a valid index between 1 and.", len(todo_list))
    except ValueError:
        print("Invalid imput. Please enter a number.")

def edit_task(todo_list):
    view_tasks(todo_list)

    if not todo_list:
        print("No tasks in the To-Do list.")
        return

    try:
        index = int(input("Enter the index of the task you want to edit: "))
        if 1 <= index <= len(todo_list):
            task = todo_list[index - 1]
            print("Current Task Details:")
            print(f"1. Task Name: {task['Task Name']}")
            print(f"2. Due Date: {task['Due Date']}")
            print(f"3. Priority: {task['Priority']}")
            
            choice = input("Enter the number corresponding to the detail you want to edit (or 0 to cancel): ")
            if choice == "1":
                task['Task Name'] = input("Enter new task name: ")
            elif choice == "2":
                task['Due Date'] = input("Enter new due date: ")
            elif choice == "3":
                task['Priority'] = input("Enter new priority: ")
            elif choice == "0":
                print("Edit canceled.")
                return
            else:
                print("Invalid choice. Edit canceled.")
                return
            print("Task edited successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(todo_list):
    view_tasks(todo_list)

    if not todo_list:
        print("No tasks in the To-Do list.")
        return

    try:
        index = int(input("Enter the index of the task you want to delete: "))
        if 1 <= index <= len(todo_list):
            del todo_list[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            edit_task(todo_list)
        elif choice == "5":
            delete_task(todo_list)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()