def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")

def view_employees():
    with open("employees.txt", "r") as file:
        print(file.read())

def search_employee():
    emp_id = input("Enter ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id):
                print("Found:", line.strip())
                return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter ID to update: ")
    lines = []
    with open("employees.txt", "r") as file:
        lines = file.readlines()

    with open("employees.txt", "w") as file:
        found = False
        for line in lines:
            if line.startswith(emp_id):
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                file.write(line)
    if not found:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter ID to delete: ")
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    with open("employees.txt", "w") as file:
        for line in lines:
            if not line.startswith(emp_id):
                file.write(line)

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        break
    else:
        print("Invalid option")
