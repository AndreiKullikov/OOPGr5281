from domain.student import Student
from domain.teacher import Teacher
from domain.account_controller import AccountController
from domain.teacher_service import TeacherService
from domain.employee import Employee



# список учителей
t1 = Teacher("Андрей", 37, "Доктор наук")
t2 = Teacher("Алексей", 35, "Кандидат наук")
t3 = Teacher("Денис", 45, "Кандидат наук")
# список студентов
s1 = Student("Денис",25)
s2 = Student("Катя",24)
s3 = Student("Тома",27)

#список работников
e1 = Employee("Виктор",35,"Разнорабочий")
e2 = Employee("Денис",37,"Разнорабочий")
e3 = Employee("Антон",38,"Разнорабочий")

teachers = [t1, t2, t3]
list_stud =[s1,s2,s3]
list_of_employees = [e1,e2,e3]

# Создание экземпляра TeacherService
teacher_service = TeacherService(teachers)

# Получаем и выводим  сортированный список учителей
sorted_teachers = teacher_service.get_sorted_persons()
print("сортированный список учителей:")
for teacher in sorted_teachers:
    print(teacher)

# Получение среднего возраста 
average_age_teachers = AccountController.averageAge(teachers)

average_age_students = AccountController.averageAge(list_stud)

average_age_employees = AccountController.averageAge(list_of_employees)

print(f"Средний возраст преподавателей: {average_age_teachers}")
print(f"Средний возраст студентов: {average_age_students}")
print(f"Средний возраст работников: {average_age_employees}")