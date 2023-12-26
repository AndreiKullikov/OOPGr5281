from typing import List
from domain.student import Student

class StudentGroup:
    def __init__(self, students: List[Student], group_id: int):
        self.students = students
        self.group_id = group_id

    def getStudents(self):
        return self.students

    def setStudents(self, students):
        self.students = students

    def getGroupId(self):
        return self.group_id

    def setGroupId(self, group_id):
        self.group_id = group_id

    def __str__(self):
        student_info = "\n".join(str(student) for student in self.students)
        return f"Group ID: {self.group_id}, Number of Students: {len(self.students)}, Students:\n{student_info}"

    def __lt__(self, other):
        # Compare based on the number of students in the group
        if len(self.students) != len(other.students):
            return len(self.students) < len(other.students)
        # If the number of students is the same, compare based on group ID
        return self.group_id < other.group_id
