# Built-in libraries
from typing import List

# Project libraries
from src.student_v2 import Student

# External libraries
import pytest
import mock


class TestStudentV2:
    @pytest.fixture
    def student(self):
        return Student(
            name='Jonas',
            age=26,
            grades=[5, 5, 10, 10]
        )

    @pytest.mark.parametrize('grades, avg_grade', zip([[10, 10], [10, 5]], [10, 7.5]))
    def test_average_grade_should_work_properly(
        self,
        student,
        grades: List[float],
        avg_grade: float
    ) -> None:
        """Average grades should work properly"""
        self.student.grades = grades

        assert student.average_grade == avg_grade

    def test_average_grade_with_empty_grades_should_return_zero(self, student) -> None:
        """Empty grades list should return zero"""
        self.student.grades = []

        assert student.average_grade == 0

    def test_average_grade_list_of_non_numerical_should_raise_error(self, student) -> None:
        """Average grades method should raise value error with non numerical list of grades"""
        with pytest.raises(ValueError):
            student.grades = ['a', 'b', 'c']

            student.average_grade

    @mock.patch('src.student_v2.datetime')
    def test_year_of_birth_should_work_properly(self, mock_datetime, student):
        """Year of birth property should work properly"""
        current_year = 2021
        mock_datetime.now.return_value.year = current_year

        expected_year_of_birth = current_year - student.age

        assert student.year_of_birth == expected_year_of_birth
