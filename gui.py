"""GUI code for the grade manager application."""

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from models import Student
from logic import get_grade, get_best_score, get_average_score
from files_handler import save_student, load_student


class GradeManagerWindow(QMainWindow):
    """Main window for the student grade manager application."""

    def __init__(self) -> None:
        """Initialize the main window and connect GUI widgets."""
        super().__init__()
        uic.loadUi("gui.ui", self)

        self.students: list[Student] = []

        self.add_button.clicked.connect(self.add_student)
        self.save_button.clicked.connect(self.save_data)
        self.load_button.clicked.connect(self.load_data)
        self.clear_button.clicked.connect(self.clear_inputs)

        self.student_table.setColumnCount(3)
        self.student_table.setHorizontalHeaderLabels(["Student", "Score", "Grade"])

        self.update_summary_labels()

    def add_student(self) -> None:
        """Add a student after validating the input."""
        name: str = self.student_name.text().strip()
        score_text: str = self.student_score.text().strip()
        if name == "":
            self.status_label.setText("Error: student name cannot be empty.")
            return

        if any(char.isdigit() for char in name):
            self.status_label.setText("Error: student name cannot contain numbers.")
            return

        try:
            score: float = float(score_text)
            if score < 0:
                raise ValueError
        except ValueError:
            self.status_label.setText("Error: score must be a non-negative number.")
            return

        new_student = Student(name, score)
        self.students.append(new_student)

        self.update_table()
        self.update_summary_labels()
        self.clear_inputs()

        self.status_label.setText("Student added successfully.")

    def update_table(self) -> None:
        """Update the table with all current student data."""
        best_score: float = get_best_score(self.students)

        self.student_table.setRowCount(len(self.students))

        for row, student in enumerate(self.students):
            grade: str = get_grade(student.get_score(), best_score)

            self.student_table.setItem(row, 0, QTableWidgetItem(student.get_name()))
            self.student_table.setItem(row, 1, QTableWidgetItem(f"{student.get_score():.2f}"))
            self.student_table.setItem(row, 2, QTableWidgetItem(grade))

    def update_summary_labels(self) -> None:
        """Update the best score and average score labels."""
        best_score: float = get_best_score(self.students)
        average_score: float = get_average_score(self.students)

        self.best_score_label.setText(f"Best Score: {best_score:.2f}")
        self.average_score_label.setText(f"Average Score: {average_score:.2f}")

    def clear_inputs(self) -> None:
        """Clear the input fields."""
        self.student_name.clear()
        self.student_score.clear()
        self.status_label.setText("Inputs cleared.")

    def save_data(self) -> None:
        """Save student data to a CSV file."""
        try:
            save_student("grades.csv", self.students)
            self.status_label.setText("Data saved successfully.")
        except OSError:
            QMessageBox.critical(self, "Save Error", "Could not save grades.csv.")

    def load_data(self) -> None:
        """Load student data from a CSV file."""
        try:
            self.students = load_student("grades.csv")
            self.update_table()
            self.update_summary_labels()
            self.status_label.setText("Data loaded successfully.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Load Error", "grades.csv was not found.")
        except ValueError:
            QMessageBox.warning(self, "Load Error", "Invalid data found in grades.csv.")
        except OSError:
            QMessageBox.critical(self, "Load Error", "Could not read grades.csv.")