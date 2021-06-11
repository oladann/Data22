class Person:
    def __init__(self, name, age = 0):
        self.name = name
        self.__age = age

    def getAge(self):
        print(self.__age)

    def _setAge(self, age):
        self.__age = age


Ola = Person("Ola", 75)

Ola._setAge(25)
Ola.getAge()