class StudentStream:
   # Инициализация объекта StudentStream.
    def __init__(self, stream_number, groups):
        self.stream_number = stream_number
        self.groups = groups

    def __str__(self): #Строковое представление объекта StudentStream.
        return f"Stream {self.stream_number}"

    def __iter__(self): #Инициализация итератора для объекта StudentStream.
        self.current_group_index = 0
        self.current_student_index = 0
        return self

    def __next__(self): #Получение следующего студента в потоке.
        if self.current_group_index < len(self.groups):
            current_group = self.groups[self.current_group_index]

            if self.current_student_index < len(current_group.getStudents()):
                current_student = current_group.getStudents()[self.current_student_index]
                student_info = f"Group ID: {current_group.getGroupId()}, {str(current_student)}"
                self.current_student_index += 1
                return student_info
            else:
                # Переход к следующей группе
                self.current_group_index += 1
                self.current_student_index = 0
                return next(self)
        else:
            raise StopIteration

    def sort_groups(self):
        self.groups.sort()