import pytest

from src.person import Person


@pytest.mark.describe('Person tests:')
class TestPerson:

    @pytest.mark.it("Person set data ok")
    def test_should_set_correct_data(self) -> None:
        name = 'Test Name'
        age = 15

        expected_dict = {
            'name': name,
            'age': age,
        }

        person = Person(name, age)

        assert person.name == 'Test'
        assert person.last_name == 'Name'
        assert person.age == age

        assert person.to_dict() == expected_dict

        assert str(person) == f'Name: {name} | Age: {age}'
