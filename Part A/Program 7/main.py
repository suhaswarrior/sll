class Student:
    def __init__(self, age, name):
        self.name = name
        self.age = age
        self.list = []

    def accept(self):
        print("Enter the marks of the students: ")
        for i in range(0, 2):
            self.list.append(int(input()))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks: ", *self.list, sep="\n")


print("Enter the details of student 1")
name = input("Enter the name: ")
age = int(input("Enter the age: "))
s1 = Student(name, age)
s1.accept()
print("Enter the details of student 2")
name = input("Enter the name: ")
age = int(input("Enter the age: "))
s2 = Student(name, age)
s2.accept()
print("\n")
print("-------Student 1---------")
s1.display()
print("-------Student 2---------")
s2.display()



