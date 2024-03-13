# '''
# Задача: Создание системы учета сотрудников для компании

# Цель: Разработать классы для управления информацией о сотрудниках в компании, включая их отделы, должности и личные данные.

# Описание:
# Класс Employee:

# Атрибуты: name (имя сотрудника), employee_id (ID сотрудника), position (должность), department (отдел).
# Методы:
# Конструктор для инициализации атрибутов.
# promote(new_position) - повышение сотрудника на новую должность.
# transfer(new_department) - перевод сотрудника в другой отдел.
# __str__() - возвращает информацию о сотруднике.


# Класс Department:

# Атрибуты: name (название отдела), department_id (ID отдела), employees (список сотрудников в отделе).
# Методы:
# Конструктор для инициализации атрибутов.
# add_employee(employee) - добавляет сотрудника в отдел.
# remove_employee(employee_id) - удаляет сотрудника из отдела.
# get_employees() - возвращает список сотрудников отдела.
# __str__() - возвращает информацию об отделе и его сотрудниках.


# Класс Company:

# Атрибуты: name (название компании), departments (список отделов в компании), employees (список всех сотрудников).
# Методы:
# Конструктор для инициализации атрибутов.
# add_department(department) - добавляет новый отдел в компанию.
# add_employee(employee, department_id) - регистрирует нового сотрудника и добавляет его в указанный отдел.
# find_employee(employee_id) - ищет сотрудника по ID.
# find_department(department_id) - ищет отдел по ID.
# transfer_employee(employee_id, new_department_id) - переводит сотрудника в другой отдел.


# Задание:
# Реализуйте вышеуказанные классы с соответствующими атрибутами и методами. Создайте взаимодействие между классами так, чтобы можно было управлять информацией о сотрудниках, их должностях и отделах. Обеспечьте возможность добавления новых сотрудников и отделов, а также перевода сотрудников между отделами и их повышения в должности.
# '''
# class Employee:
#     def __init__(self, name, employee_id, position, department):
#         self.name = name
#         self.employee_id = employee_id
#         self.position = position
#         self.department = department

#     def promote(self, new_position):
#         self.position = new_position
#     def transfer(self, new_department):
#         self.department = new_department
    
#     def __str__(self):
#         return f'{self.name}(id: {self.employee_id}) is {self.position} at {self.department}- department'

# em1 = Employee('Nursultan', 12, 'boss', 'Taxes')
# em1.promote('CEO')
# em1.transfer('OPtima')
# # print(em1)

# class Department:
#     def __init__(self, name, department_id, employees = []):
#         self.name = name
#         self.dep = department_id
#         self.empl = employees
#     def add_employee(self, employee):
#         self.empl.append(employee)
#     def remove_employee(self, employee_id):
#         for employee in self.empl:
#             if employee.employee_id == employee_id:
#                 self.empl.remove(employee)
#     def get_employees(self):
#         return f'{self.empl}'
#     def __str__(self):
#         return f'{self.name}(id: {self.dep}) has employees({[i.name for i in self.empl]})'

# em2 = Employee('Nurba', 13, 'Officer', 'Taxes')   
# dep = Department('Optima', 10, [em1, em2])
# dep.add_employee(em1)
# dep.remove_employee(12)
# dep.get_employees()
# print(dep)

class Employee:
    def init(self, name, employee_id, position, department):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.department = department

    def promote(self, new_position):
        self.position = new_position
    def transfer(self, new_department):
        self.department = new_department
    
    def str(self):
        return f'{self.name}(id: {self.employee_id}) is {self.position} at {self.department}- department'


# print(em1)

class Department:
    def init(self, name, department_id, employees = []):
        self.name = name
        self.dep = department_id
        self.empl = employees

    def add_employee(self, employee):
        self.empl.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.empl:
            if employee.employee_id == employee_id:
                self.empl.remove(employee)

    def get_employees(self):
        return f'{self.empl}'
    
    def str(self):
        return f'{self.name}(id: {self.dep}) has employees({[i.name for i in self.empl]})'


class Company:
    def init(self, name, employees=[], departments=[]) -> None:
        self.name = name
        self.empl = employees
        self.departments = departments

    def add_department(self, department):
        self.departments.append(department)

    def add_employee(self, employee, department_id):
        if self.departments:
            for dep in self.departments:
                if dep.dep == department_id:
                    dep.add_employee(employee)
                    self.empl.append(employee)
        else:
            return 'Такого отдела нет!'
    
    def find_employee(self, employee_id):
        if self.empl:
            for emp in self.empl:
                if emp.employee_id == employee_id:
                    return emp.name
        else:
            return 'Такого сотрудника нет!'  
        

    def find_department(self, department_id):
        if self.departments:
            for dep in self.departments:
                if dep.dep == department_id:
                    return dep.name
                
        else:
            return 'Not found department!'
    
    def transfer_employee(self, employee_id, new_department_id):
        if self.empl:
            for em in self.empl:
                if em.employee_id == employee_id:
                    for dep in self.departments:
                        if dep.dep == new_department_id:
                            em.transfer(dep)
        else:
            return 'Not found employe!'
        
    def str(self) -> str:
        return f'Все сотрудники -> {[[i.name, i.department.name]   for i in self.empl]}\nВсе департаменты -> {[i.name for i in self.departments]}'


        


it = Department('IT', 1)
marketing = Department('Marketing', 2)
clining = Department('Clining', 3) 


altai = Employee('Altai', 1, 'boss', clining)
anarbek = Employee('Anarbek', 2, 'boss', marketing)
temirlan = Employee('Temirlan', 3, 'boss', it)


codify = Company('Codify')

codify.add_department(it)
codify.add_department(marketing)
codify.add_department(clining)

codify.add_employee(altai, 1)


print(codify)
codify.transfer_employee(1, 1)
print(codify)

# class Company:
#     def __init__(self, name, departments = [], employees = []):
#         self.name = name
#         self.departments = departments
#         self.emp = employees

#     def add_department(self, department): 
#         self.departments.append(department)

#     def add_employee(self, employee, department_id):
#         department = self.find_department(department_id)
#         if department:
#             department["employees"].append(employee)
#             self.emp.append(employee)
#             print(f"Employee {employee['name']} added to department {department_id}.")
#         else:
#             print(f"Department with ID {department_id} not found.")

#     def find_employee(self, employee_id):
#         for employee in self.emp:
#             if employee["id"] == employee_id:
#                 return employee

#     def find_department(self, department_id):
#         for department in self.departments:
#             if department["id"] == department_id:
#                 return department

#     def transfer_employee(self, employee_id, new_department_id):
#         employee = self.find_employee(employee_id)
#         if employee:
#             new_department = self.find_department(new_department_id)
#             if new_department:
#                 old_department = self.find_department(employee["department_id"])
#                 old_department["employees"].remove(employee)
#                 new_department["employees"].append(employee)
#                 employee["department_id"] = new_department_id
#                 print(f"Employee {employee_id} transferred to department {new_department_id}.")
#             else:
#                 print(f"Department with ID {new_department_id} not found.")
#         else:
#             print(f"Employee with ID {employee_id} not found.")

#     def __str__(self):
#         return f"Company: {self.name}, Departments: {self.departments}"


# com = Company('Quewee', [{'id': 1, 'name': 'Marketing', 'employees': []}])
# com.add_department({'id': 2, 'name': 'Optima', 'employees': []})

# employee1 = {'id': 1, 'name': 'Misha', 'department_id': 1}
# com.add_employee(employee1, 1)

# print(com)
# com.transfer_employee(1, 2)
# print(com)

