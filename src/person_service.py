import pandas

from src.person import Person


class PersonService:

    def __init__(self) -> None:
        self.__csv_path = './person.csv'

    def create_person_by_csv_file(self) -> list:
        person_df = self._read_person_csv()
        created_persons = []

        for index, row in person_df.iterrows():
            created_persons.append(Person(
                name=row['NAME'],
                age=row['AGE'],
            ))

        return created_persons

    def _read_person_csv(self) -> pandas.DataFrame:
        return pandas.read_csv(self.__csv_path)
