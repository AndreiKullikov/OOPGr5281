
from domain.student import Student
from domain.student_group import StudentGroup
from domain.student_stream import StudentStream


s1 = Student("Иван", 25)
s2 = Student("Игорь", 23)
s3 = Student("Иван", 22)
s4 = Student("Игорь", 23)
s5 = Student("Даша", 23)
s6 = Student("Лена", 23)
s7 = Student("Катя", 25)
s8 = Student("Андрей", 27)
s9 = Student("Илья", 22)
s10 = Student("Алексей", 29)
s11 = Student("Карина", 28)
s12 = Student("Марина", 25)
s13 = Student("Тома", 25)
s14 = Student("Сергей", 23)
s15 = Student("Борис", 19)
s16 = Student("Артур", 23)
s17 = Student("Виталий", 22)
s18 = Student("Александр", 18)
s19 = Student("Иван", 25)
s20 = Student("Игорь", 25)
s21 = Student("Иван", 22)
s22 = Student("Карина", 21)
s23 = Student("Тома", 26)
s24 = Student("Лена", 23)


group4580 = StudentGroup([s1, s2, s3, s4, s5, s6],4580)
print(group4580)

group4581 = StudentGroup([s7,s17, s8,s9,s10,s11,s12,s13,s14,s15],4581)
print(group4581)

group4582 = StudentGroup([s16,s18,s19,s20,s21,s22,s23,s24],4582)
print(group4582)


print("=========================================================")

# sorted_group = sorted(group4580.getGroup(), key=lambda student: student.age)

sorted_group1 = sorted(group4580.getStudents(), key=lambda student: student.getAge())
sorted_group2 = sorted(group4581.getStudents(), key=lambda student: student.getAge())
sorted_group3 = sorted(group4582.getStudents(), key=lambda student: student.getAge())

sorted_group4580 = StudentGroup(sorted_group1, group4580.getGroupId())
sorted_group4581 = StudentGroup(sorted_group2, group4581.getGroupId())
sorted_group4582 = StudentGroup(sorted_group3, group4582.getGroupId())

stream = StudentStream(101, [group4580, group4581, group4582])
stream1 = StudentStream(101, [sorted_group4580, sorted_group4581, sorted_group4582])

    # Отображение групп в потоке с помощью интерфейса Iterable
print("Все группы в потоке:")
for group in stream:
        print(group)

    # Сортировка групп в потоке
stream1.sort_groups()

    # Отображение отсортированных групп в потоке
print("\nОтсортированные группы в потоке:")
for group in stream1:
        print(group)