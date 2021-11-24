class Person:

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'Name: {self.name} | Age: {self.age}'
