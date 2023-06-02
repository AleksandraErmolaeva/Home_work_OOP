class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade(self):        
        self.new_grades = {}
        for x in self.grades:
            self.new_grades[x] = self.grades[x][0]
        self.y_grades = []
        for one_grade in  self.new_grades.values():
            self.y_grades.append(int(one_grade))
            self.av_grade = sum(self.y_grades)/len(self.y_grades)
        print(self.av_grade)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Преподавателей и студентов нельзя сравнить'
        return self.av_grade < other.av_grade


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

   

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades  = {}

    def average_grade(self):
        self.new_grades = {}
        for x in self.grades:
            self.new_grades[x] = self.grades[x][0]
        self.y_grades = []
        for one_grade in  self.new_grades.values():
            self.y_grades.append(int(one_grade))
            self.av_grade = sum(self.y_grades)/len(self.y_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Преподавателей и студентов нельзя сравнить'
        return self.av_grade < other.av_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}'
        
class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and  course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
     def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
        

student_1 = Student('Bob', 'Johnson', 18)
student_2 = Student ('Emma', 'Brown',17)

lecturer_1 = Lecturer('John', 'Khan')
lecturer_2 = Lecturer('Anna', 'Black')

reviewer_1 = Reviewer('Lily', 'Oldwin')
reviewer_2 = Reviewer('Barney', 'Stinckson')

student_1.add_courses('Java')
student_2.add_courses('Java')

student_1.courses_in_progress += ['Python', 'Введение в программирование']
student_2.courses_in_progress += ['Python', 'Full-stuck']

reviewer_1.rate_hw(student_1, 'Python', '7')
reviewer_2.rate_hw(student_1, 'Введение в программирование', '9')
reviewer_1.rate_hw(student_2, 'Python', '9')
reviewer_2.rate_hw(student_2, 'Full-stuck', '10')


lecturer_1.courses_attached = ['Python', 'Java']
lecturer_2.courses_attached = ['Введение в программирование', 'Full-stuck']

student_1.rate_hw(lecturer_1, 'Python', '8')
student_1.rate_hw(lecturer_1, 'Java', '1')
student_2.rate_hw(lecturer_1, 'Python', '4')
student_2.rate_hw(lecturer_1, 'Java', '5')
student_2.rate_hw(lecturer_1, 'Full-stuck', '7')

student_1.rate_hw(lecturer_2, 'Введение в программирование', '8')
student_1.rate_hw(lecturer_2, 'Full-stuck', '9')
student_2.rate_hw(lecturer_2, 'Введение в программирование', '10')
student_2.rate_hw(lecturer_2, 'Full-stuck', '7')

student_1.average_grade()
student_2.average_grade()

lecturer_1.average_grade()
lecturer_2.average_grade()

print(student_1)
print(student_2)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print(student_1<student_2)
print(lecturer_1<lecturer_2)

def average_students(students, name_of_course):
    all_grades = []
    for student in students:
       all_grades += student.grades.get(name_of_course,[])
    all_grades_nums = [int(el) for el in all_grades]
       
    if len(all_grades) == 0:
        print(f'За курс {name_of_course} нет оценок')
    else:
        average_grade = sum(all_grades_nums)/len(all_grades_nums)
        print(average_grade)
    
    
list_of_students = [student_1,student_2]       
average_students(list_of_students, 'Python')
average_students(list_of_students, 'Java')
average_students(list_of_students, 'Введение в программирование')

def average_lecturer(lecturers, name_of_course):
    all_grades = []
    for lecturer in lecturers:
        all_grades += lecturer.grades.get(name_of_course,[])
    all_grades_nums = [int(el) for el in all_grades]
    if len(all_grades_nums) == 0:
        print(f'За курс {name_of_course} нет оценок')
    else:
        average_grade = sum(all_grades_nums)/len(all_grades_nums)
        print(average_grade)

list_of_lecturers = [lecturer_1, lecturer_2]
average_lecturer(list_of_lecturers, 'Python')
average_lecturer(list_of_lecturers, 'Java')
average_lecturer(list_of_lecturers, 'Введение в программирование')



