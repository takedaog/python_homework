import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        task = next((task for task in self.tasks if task.task_id == task_id), None)
        if task:
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            task.due_date = input("Enter new due date: ")
            task.status = input("Enter new status: ")
            print("Task updated!")
        else:
            print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        task = next((task for task in self.tasks if task.task_id == task_id), None)
        if task:
            self.tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found.")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(**task_data)
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No tasks file found, starting with an empty list.")

# Example usage
app = ToDoApp()
app.add_task()
app.view_tasks()
app.save_tasks()
app.load_tasks()
app.delete_task()
