class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        with open(self.filename, "a") as file:
            file.write(str(employee) + "\n")

    def view_all_employees(self):
        with open(self.filename, "r") as file:
            print("Employee Records:")
            for line in file:
                print(line.strip())

    def search_employee(self, employee_id):
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith(employee_id):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        lines = []
        with open(self.filename, "r") as file:
            lines = file.readlines()

        with open(self.filename, "w") as file:
            found = False
            for line in lines:
                if line.startswith(employee_id):
                    if name: line = f"{employee_id}, {name}, {position or ''}, {salary or ''}\n"
                    found = True
                file.write(line)
        if not found:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        lines = []
        with open(self.filename, "r") as file:
            lines = file.readlines()

        with open(self.filename, "w") as file:
            for line in lines:
                if not line.startswith(employee_id):
                    file.write(line)

# Example usage
manager = EmployeeManager()
emp1 = Employee(1001, "John Doe", "Software Engineer", 75000)
manager.add_employee(emp1)
manager.view_all_employees()
manager.search_employee(1001)
manager.update_employee(1001, name="Johnathan Doe")
manager.delete_employee(1001)
