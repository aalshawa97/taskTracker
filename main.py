class Task:
    def __init__(self, title, description, due_date, status="To Do"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

def create_task(title, description, due_date):
    task = Task(title, description, due_date)
    print("Task created successfully!")
    return task

def update_task(tasks, task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index")
        return
    task = tasks[task_index]
    option = input("Would you like to change the"
          " (1) Title"
          " (2) Description"
          " (3) Date? ")
    if option == "1":
        new_title = input("Enter the new title: ")
        task.title = new_title
    elif option == "2":
        new_description = input("Enter the new description: ")
        task.description = new_description
    elif option == "3":
        new_date = input("Enter the new due date: ")
        task.due_date = new_date
    else:
        print("Invalid input")
    #print_task_details(task)

def print_hi(name):
    print(f'Hi, {name}')

def print_task_details(task):
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date}")
    print(f"Status: {task.status}")

def print_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task {index}:")
            print_task_details(task)
            print()

if __name__ == '__main__':
    print_hi('PyCharm')
    tasks = []  # Initialize an empty list to store tasks
    task = create_task("Coding", "Learn Cloud Computing0", "7/3")
    tasks.append(task)  # Add the created task to the list
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task you want to update: "))
    update_task(tasks, task_index)
    print_tasks(tasks)
