from src.person_service import PersonService


if __name__ == "__main__":
    for person in PersonService().create_person_by_csv_file():
        print(person)
