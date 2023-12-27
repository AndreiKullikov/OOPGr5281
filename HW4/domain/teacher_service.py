from typing import List
from domain.teacher import Teacher
from comparator.person_comparator import PersonComparator

class TeacherService:
    def __init__(self, teachers: List[Teacher]):
        self.teachers = teachers

    def get_sorted_persons(self) -> List[Teacher]:
        return sorted(self.teachers, key=lambda teacher: PersonComparator.compare_persons_key(teacher))