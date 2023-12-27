from typing import Union
from domain.person import Person
from domain.student import Student
from domain.teacher import Teacher
from domain.employee import Employee

class PersonComparator:
    @staticmethod
    def compare_persons(person1: Union[Person, Student, Teacher, Employee], person2: Union[Person, Student, Teacher, Employee]) -> int:
        age1 = person1.getAge()
        age2 = person2.getAge()

        if age1 < age2:
            return -1
        elif age1 > age2:
            return 1
        else:
            return 0

    @staticmethod
    def compare_persons_key(person):
        return person.getAge()