class Person:
    firstName = ""
    lastName = ""
    birthDate = ""
    __city = ""
    __password = ""

    def __init__(self,firstName, lastName, birthDate, city, password):
        Person.firstName = firstName
        Person.lastName = lastName
        Person.birthDate = birthDate
        Person.__city = city
        Person.__password = password

    def __str__(self):
        return f"Name: \t {Person.firstName}\nSurname: {Person.lastName}\nBirth date: {Person.birthDate}\n"

    def getCity(self):
        return Person.__city

    def setCity(self, city):
        Person.__city = city

    def getPassword(self):
        return Person.__password

    def setPassword(self, password):
        Person.__city = password

    def changePassword(self, password, newPassword):
        if Person.__password == password:
            Person.__password = newPassword

    def getFirstName(self):
        return Person.firstName

    def setFirstName(self, name):
        Person.firstName = name

    def getLastName(self):
        return Person.lastName

    def setLastName(self, name):
        Person.lastName = name

    def getBirthDate(self):
        return Person.birthDate

    def setBirthDate(self, date):
        Person.birthDate = date

Stepan = Person("Stepan", "Shevchenko", "1.01.1993", "Kiev", "StepanB1939")

print(Stepan)