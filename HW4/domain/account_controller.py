from typing import List, Union
from domain.student import Student
from domain.teacher import Teacher
from domain.employee import Employee

class AccountController:
    @staticmethod
    def averageAge(persons: List[Union[Student, Teacher, Employee]]) -> float:
        if not persons:
            return 0.0

        total_age = sum(person.getAge() for person in persons)
        return total_age / len(persons)