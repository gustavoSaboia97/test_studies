from src.person import Person


class Student(Person):

    def __init__(self, grades: list) -> None:
        self.__grades = grades

    @property
    def general_grade(self) -> str:
        return sum(self.__grades)/len(self.__grades)
