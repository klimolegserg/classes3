class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def midgrade_st(self):
        values_st = self.grades.values()
        values_list = list(values_st)
        average = sum(values_list)/len(values_list)
        return average

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашнее задание: {self.averege()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return self == other
    
    def __it__(self, other):
        return self < other
    
    def __gt__(self, other):
        return self > other   

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
           
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def midgrade_st(self):
        values_st = self.grades.values()
        values_list = list(values_st)
        average = sum(values_list)/len(values_list)
        return average

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.average()}'
    
    def __eq__(self, other):
        return self == other
    
    def __it__(self, other):
        return self < other
    
    def __gt__(self, other):
        return self > other
  

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        
    def rate_nw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)