import json

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = float(salary)

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def average(self):
        if not self.employees:
            return 0
        else:
            total_salary = sum(employee.salary for employee in self.employees)
            return total_salary / len(self.employees)

    def max(self):
        if not self.employees:
            return None
        else:
            return max(self.employees, key=lambda employee: employee.salary)

    def min(self):
        if not self.employees:
            return None
        else:
            return min(self.employees, key=lambda employee: employee.salary)

    def positions(self):
        position_count = {}
        for employee in self.employees:
            if employee.position in position_count:
                position_count[employee.position] += 1
            else:
                position_count[employee.position] = 1
        return position_count

def read_json_file(filename):
    with open(filename) as file:
        try:
            return json.load(file)
        except FileNotFoundError:
            print(f"No such file or directory")

def main():
    data = read_json_file('homework22/data.json')

    departments = []
    for key, dept_data in data.items():
        employees = [Employee(emp['name'], emp['position'], emp['salary']) for emp in dept_data['employees']]
        department = Department(dept_data['name'], employees)
        departments.append(department)

    for dept in departments:
        print(f"Department: {dept.name}")
        print(f"Average Salary: {dept.average()}")
        
        max_salary_employee = dept.max()
        if max_salary_employee:
            print(f"Max Salary: {max_salary_employee.name}, {max_salary_employee.salary}")
            
        min_salary_employee = dept.min()
        if min_salary_employee:
            print(f"Min Salary: {min_salary_employee.name}, {min_salary_employee.salary}")
            
        print(f"Positions: {dept.positions()}")
        print()

if __name__ == "__main__":
    main()

        