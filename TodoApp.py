tasks = []

def task_fun():
    print("Welcome to Task Manager App")
    task = int(input("How many tasks do you want to add: "))
    for i in range(1, task + 1):
        task_list = input(f"The task is {i}: ")
        tasks.append(task_list)

    while True:
        print("1. List Task")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit app")
        choice = input("Select the option: ")
        if choice == '1':
            print(tasks)
        elif choice == '2':
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(tasks)
        elif choice == '3':
            up = input("Enter the task you want to update: ")
            new_task = input("Enter the new task you want to add: ")
            if up in tasks:
                task_number = tasks.index(up)
                tasks[task_number] = new_task
                print(tasks)
            else:
                print("Task not found!")
        elif choice == '4':
            delete = input("Enter the task you want to delete: ")
            if delete in tasks:
                tasks.remove(delete)
                print(tasks)
            else:
                print("Task not found!")
        elif choice == '5':
            print("App is closing...")
            break
        else:
            print("Invalid option. Please try again.")

task_fun()