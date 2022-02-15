from Mentor import Mentor


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_rating(self):
        list_ratings = list(self.grades.values())
        list_ratings = sum(list_ratings, [])

        if list_ratings:
            return round(sum(list_ratings) / float(len(list_ratings)), 1)
        else:
            return 0

    def __str__(self):

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.get_average_rating()}'

    #Реализованы только 2 метода: "больше" и "меньше". Остальные методы
    #реализуются аналогично...
    def __lt__(self, other):

        if isinstance(other, Lector):
            return self.get_average_rating() < other.get_average_rating()

    def __gt__(self, other):
        if isinstance(other, Lector):
            return self.get_average_rating() > other.get_average_rating()