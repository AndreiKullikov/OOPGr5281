from typing import List

class StudentGroup:
    def __init__(self, group_id: int, students: List[str]):
        self.group_id = group_id
        self.students = students

    def __str__(self):
        return f"Group ID: {self.group_id}, Number of Students: {len(self.students)}, Students: {self.students}"

    def __lt__(self, other):
        # Compare based on the number of students in the group
        if len(self.students) != len(other.students):
            return len(self.students) < len(other.students)
        # If the number of students is the same, compare based on group ID
        return self.group_id < other.group_id


class StudentStream:
    def __init__(self, stream_number: int, groups: List[StudentGroup]):
        self.stream_number = stream_number
        self.groups = groups

    def __str__(self):
        return f"Stream Number: {self.stream_number}, Number of Groups: {len(self.groups)}, Groups: {self.groups}"

    def __iter__(self):
        # Implementing Iterable interface
        return iter(self.groups)

    def sort_groups(self):
        # Sorting groups in the stream first by the number of students and then by group ID
        self.groups.sort()


# Example usage:
if __name__ == "__main__":
    group15 = StudentGroup(1, ["John", "Alice"])
    group256 = StudentGroup(2, ["Bob", "Charlie", "David"])
    group314 = StudentGroup(3, ["Eve"])

    stream = StudentStream(101, [group314, group15, group256])

    # Display groups in the stream using the Iterable interface
    print("Groups in the stream:")
    for group in stream:
        print(group)

    # Sort groups in the stream
    stream.sort_groups()

    # Display sorted groups in the stream
    print("\nSorted groups in the stream:")
    for group in stream:
        print(group)
