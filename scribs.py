#!/usr/bin/python3
name = 'peter'
password = 'pass'


class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f'I {self.name} have logged into the school')


class Lecturer(User):
    def __init__(self, name):
        super().__init__(name)

    def mark_exam(self):
        print('I am marking the exam')


class Student(User):
    def __init__(self, name):
        super().__init__(name)

    def do_exam(self):
        print('I am doing the exam')


lecturer1 = Lecturer('Mutas')
student1 = Student('Richard')

lecturer1.login()
student1.login()
