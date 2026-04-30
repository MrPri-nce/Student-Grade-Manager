"""Functions for saving and loading student data."""

import csv
from models import Student

def save_student(filename: str, students: list[Student])-> None:
    """saves the student data to a csv file"""
    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Score'])
        for student in students:
            writer.writerow([student.get_name(), student.get_score()])


def load_student(filename: str) -> list[Student]:
    """loads the student data from a csv file"""
    students = []

    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader)

        for row in reader:
            if len(row) == 2:
                name = row[0]
                score = float(row[1])
                students.append(Student(name, score))
    return students

