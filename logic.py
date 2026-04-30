"""Letter grading logic for the grading manager app"""

from models import Student

def get_grade(score: float, best_score: float)-> str:
    """returns the grade of the student"""
    score = float(score)
    best_score = float(best_score)
    if score >= best_score -10:
        return 'A'

    if score >= best_score -20:
        return 'B'

    if score >= best_score -30:
        return 'C'

    if score >= best_score -40:
        return 'D'

    return 'F'

def get_best_score(students: list[Student])-> float:
    """returns the best score of the students"""
    if not students:
        return 0.0
    return max(student.get_score() for student in students)


def get_average_score(students: list[Student])-> float:
    """returns the best score of the students"""
    if not students:
        return 0.0
    total = sum(student.get_score() for student in students)
    return total / len(students)

