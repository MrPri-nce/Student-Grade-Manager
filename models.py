"""Classes and models for the grade manager app"""

class Student:
    """student model representing a student and score"""

    def __init__(self, name: str, score: float) -> None:
        """initializes a student object"""
        self.__name = name
        self.__score = score

    def get_name(self):
        """Returns the name of the student"""
        return self.__name

    def get_score(self):
        """Returns the score of the student"""
        return self.__score

    def set_name(self, name: str) -> None:
        """Sets the name of the student"""
        self.__name = name

    def set_score(self, score: float) -> None:
        """sets the score of the student"""
        self.__score = score
