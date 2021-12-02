from src.student import Student

import pytest


class TestStudent:
    GRADES = [8., 9., 10., 8.6]

    @pytest.fixture(autouse=True)
    def student(self):
        return Student(
            person=None,
            grades=self.GRADES
        )

    def setup(self):
        self.mock_person = mock.MagicMock()

        self.student = Student(
            person=mock_person,
            grades=self.GRADES
        )

    def test_person_property_should_work_properly(self) -> None:
        """"""
        assert self.student.person == self.mock_person

    @pytest.mark.parametrize('age', [10, 20, 30])
    def test_person_age_getter_should_work_properly(self, age: int) -> None:
        """"""
        self.mock_person.age = age

        assert self.student.age == age

    @pytest.mark.parametrize('grades, avg_grade', zip([[10,10], [10, 5]], [10, 7.5]))
    def test_average_grade_should_work_properly(self, grades: List[float] , avg_grade: float) -> None:
        """"""
        self.student.grades = grades

        assert student.average_grade() == avg_grade

    def test_average_grade_with_empty_grades_should_return_zero(self) -> None:
        """"""
        self.student.grades = []

        assert student.average_grade() == 0

    def test_average_grade_with_should_return_expected_value(self) -> None:
        """"""
        ...

    def test_average_grade_list_of_non_numerical_should_raise_error(self) -> None:
        """"""
        with pytest.raises(ValueError):
            self.student.grades = ['a', 'b', 'c']

            self.student.average_grade()