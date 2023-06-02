# from typing import Tuple


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__ageInFiveYears = age + 5

    def doSomethingGetString(self) -> str:
        return self.name + " is doing something"

    def __str__(self) -> str:
        return (
            self.name
            + " is "
            + str(self.age)
            + " years old. And will be "
            + str(self.__ageInFiveYears)
            + " in 5 years."
        )


def main():
    persona: Person

    persona = Person("John", 20)

    print(persona)
    print(persona.name)
    print(persona.age)

    print(persona.doSomethingGetString())


if __name__ == "__main__":
    main()
