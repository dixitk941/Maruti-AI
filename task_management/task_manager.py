tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for task in tasks:
        print(task)
