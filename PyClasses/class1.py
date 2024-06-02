class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def show_role(self):
        if self.role:
            print(f"{self.name} is {self.age} and a/an {self.role}")


class Manager(Person):
    def my_role(self):
        print(f"The role of a {self.role}:")
        print("1. Set Objectives")
        print("2. Analyze")
        print("3. Lead and")
        print("4. Make decisions")
        print("5. Review")


class Employee(Person):
    def my_role(self):
        print(f"{self.role}'s role is specific to what the {self.role} is employed to do")


person1 = Manager("Miss Shaukat", 20, "Manager")
person1.show_role()
person1.my_role()
person2 = Employee("Miss Ekua", 19, "Employee")
person2.show_role()
person2.my_role()
