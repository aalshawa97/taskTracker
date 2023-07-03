class Task:
    def __init__(self, title, description, due_date, status="To Do"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

def create_task(title, description, due_date):
    task = Task(title, description, due_date)
    print("Task created successfully!")

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    create_task("Marriage", "Nikkah", "7/3")
