tasks = []

def task():
    print("Task Management App")
    number = int(input("Enter how many task you want to add: "))
    for i in range(1, number + 1):
        task_item = input(f"the task {i}: ")
        tasks.append(task_item)

    while True:
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter the task to add: ")
            tasks.append(new_task)
            print(f"Updated task list: {tasks}")
        elif choice == '2':
            update_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            if update_task in tasks:
                ind = tasks.index(update_task)
                tasks[ind] = new_task

            else:
                print("the task you want to update can not exit in list")
            print(f"Updated task list: {tasks}")
        elif choice=='3':
            delete_task=input("enter task to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
            else:
                print("the task you want to delete can not exit in list")
            print(f"the task list after deletion is {tasks}")
        elif choice=='4':
            print("the app is closing....")
            break
        else:
            print("chose invalid option")
task()