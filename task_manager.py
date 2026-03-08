class Task:
    def __init__(task, id, title, description, status):
        task.id = id
        task.title = title
        task.description = description
        task.status = status
tasks = []
id = 1
def addTask():
    global id
    title = input("Enter task name: ")
    description = input("What is it about: ")
    status = "Pending"
    new_task = Task(id, title, description, status)
    tasks.append(new_task)
    id = id + 1

def list_tasks():
    for task in tasks:
        print(f"{task.id} | {task.title} | {task.description} | {task.status}")

def mark_completed(taskId):
    for task in tasks:
        if task.id == taskId:
            task.status = "Completed"
            return
    print("No such task")

def deleteTask(taskId):
    for task in tasks:
        if task.id == taskId:
            tasks.remove(task)
            return
    print("No such task")

def addToFile(filename = "tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task.id}|{task.title}|{task.description}|{task.status}\n")

def loadFromFile():
    global tasks
    global id
    tasks = []
    with open("tasks.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")

            id = int(parts[0])
            title = parts[1]
            description = parts[2]
            status = parts[3]

            task = Task(id, title, description, status)
            tasks.append(task)



while True:
    print("\n--- TASK MANAGER ---")
    print("1 - Add Task")
    print("2 - List Tasks")
    print("3 - Mark Completed")
    print("4 - Delete Task")
    print("5 - Save Tasks")
    print("6 - Load Tasks")
    print("7 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        addTask()

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        taskId = int(input("Enter task ID: "))
        mark_completed(taskId)

    elif choice == "4":
        taskId = int(input("Enter task ID: "))
        deleteTask(taskId)

    elif choice == "5":
        addToFile()

    elif choice == "6":
        loadFromFile()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
    

