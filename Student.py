from Lector import Lector

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if (isinstance(lector, Lector) and course in lector.courses_attached
                and course in self.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_rating(self):
        list_ratings = list(self.grades.values())
        list_ratings = sum(list_ratings, [])

        if list_ratings:
            return round(sum(list_ratings) / float(len(list_ratings)), 1)
        else:
            return 0

    def __str__(self):

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.get_average_rating()}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'

    # Реализованы только 2 метода: "больше" и "меньше". Остальные методы
    # реализуются аналогично...
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_rating() < other.get_average_rating()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_rating() > other.get_average_rating()
