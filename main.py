from Student import Student
from Lector import Lector
from Reviewer import Reviewer


def get_average_rating(lst_items, course_name):

    all_grades = []
    for item in lst_items:
        try:
            all_grades += item.grades[course_name]
        except KeyError:
            pass

    if all_grades:
        return round(sum(all_grades) / float(len(all_grades)), 1)
    else:
        return 0




def main():

    student_martin = Student('Martin', 'Green', 'Male')
    student_alice = Student('Alice','Brown', 'Female')

    lector_smith = Lector('Jho', 'Smith')
    lector_miller = Lector('Andrew', 'Miller')

    reviewer_wilson = Reviewer('Sam', 'Wilson')
    reviewer_bell = Reviewer('James', 'Bell')

    student_martin.finished_courses += ['linux', 'Cisco']
    student_martin.courses_in_progress += ['Python', 'JavaScript', 'CSS']

    student_alice.finished_courses += ['linux']
    student_alice.courses_in_progress += ['Python', 'JavaScript']

    lector_miller.courses_attached += ['CSS']
    lector_smith.courses_attached += ['Python', 'CSS']

    reviewer_wilson.courses_attached += ['JavaScript']
    reviewer_bell.courses_attached += ['Python', 'CSS']

    student_martin.rate_lecture(lector_smith, 'Python', 1)
    student_alice.rate_lecture(lector_smith, 'Python', 6)
    student_martin.rate_lecture(lector_smith,'CSS', 5)

    reviewer_bell.rate_hw(student_martin,'Python', 10)
    reviewer_bell.rate_hw(student_martin, 'CSS', 6)

    reviewer_bell.rate_hw(student_alice, 'Python', 2)
    reviewer_bell.rate_hw(student_martin, 'Python', 5)
    reviewer_bell.rate_hw(student_martin, 'CSS', 5)


    #print(student_alice < student_martin)
    print(get_average_rating([student_martin, student_alice], 'CSS'))
    print('/////////////////////////')
    print(get_average_rating([lector_smith, lector_miller], 'Python'))
    print('/////////////////////////')
    print(lector_smith)
    print('/////////////////////////')
    print(reviewer_bell)
    print('/////////////////////////')
    print(student_martin)


main()




















