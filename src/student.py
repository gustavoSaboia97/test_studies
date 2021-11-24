from src.person import Person


class Student:

    def __init__(self, person: Person, grades: list) -> None:
        self.__person = person
        self.__grades = grades

    @property
    def person(self) -> Person:
        return self.__person

    @property
    def general_grade(self) -> str:
        return sum(self.__grades)/len(self.__grades)
