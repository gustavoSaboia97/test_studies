from typing import List

from src.person import Person


class Student:

    def __init__(self, person: Person, grades: List[float]) -> None:
        self.__person = person
        self.__grades = grades

    @property
    def person(self) -> Person:
        return self.__person

    @property
    def age(self) -> int:
        return self.person.age

    @property
    def grades(self) -> List[float]:
        return self.__grades

    @grades.setter
    def grades(self, value):
        if isinstance(value, List[float]):
            self.__grades = value
        else:
            raise ValueError(f"Expected a list of floats, but got {type(value)}")

    @property
    def average_grade(self) -> str:
        return sum(self.__grades)/len(self.__grades)
