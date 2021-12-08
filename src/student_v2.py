from datetime import datetime

from src.person import Person


class Student(Person):

    def __init__(
        self,
        name: str,
        age: int,
        grades: list
    ) -> None:
        super().__init__(name=name, age=age)
        self.__grades = grades

    @property
    def general_grade(self) -> str:
        return sum(self.__grades)/len(self.__grades)

    @property
    def year_of_birth(self):
        current_year = datetime.now().year

        return current_year - self.age