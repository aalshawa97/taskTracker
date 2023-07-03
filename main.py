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

def update_task(task):
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
    print_task_details(task)

def print_hi(name):
    print(f'Hi, {name}')

def print_task_details(task):
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date}")
    print(f"Status: {task.status}")

if __name__ == '__main__':
    print_hi('PyCharm')
    task = create_task("Python", "Learn Classes", "7/3")
    update_task(task)
