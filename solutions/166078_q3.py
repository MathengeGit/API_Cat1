# Employee and Department Management
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"{self.name} (ID: {self.employee_id}) - Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()

if __name__ == "__main__":
    dept = Department("Engineering")
    emp1 = Employee("David", "E001", 50000)
    emp2 = Employee("Eva", "E002", 60000)

    dept.add_employee(emp1)
    dept.add_employee(emp2)

    dept.display_all_employees()
    dept.total_salary_expenditure()
    emp1.update_salary(55000)
    dept.total_salary_expenditure()
