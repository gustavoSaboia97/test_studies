class Person:

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

        self.__last_name = None

    @property
    def name(self) -> str:
        values = self.__name.split(' ')

        if len(values) > 1:
            self.__last_name = values[-1]

        return values[0]

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def age(self) -> int:
        return self.__age

    def to_dict(self) -> dict:
        return {
            'name': self.__name,
            'age': self.__age,
        }

    def __str__(self) -> str:
        return f'Name: {self.__name} | Age: {self.__age}'
