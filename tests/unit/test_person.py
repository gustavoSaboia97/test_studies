import pytest

from src.person import Person


@pytest.mark.describe('Person tests:')
class TestPerson:

    @pytest.mark.it("Person set data ok")
    def test_should_set_person_data(self) -> None:
        name = 'Test Name'
        age = 15

        person = Person(name, age)

        assert person.name == name
