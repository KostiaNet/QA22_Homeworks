# class Person:
#     firstName = ""
#     lastName = ""
#     birthDate = ""
#     __city = ""
#     __password = ""
#
#     def __init__(self,firstName, lastName, birthDate, city, password):
#         Person.firstName = firstName
#         Person.lastName = lastName
#         Person.birthDate = birthDate
#         Person.__city = city
#         Person.__password = password
#
#     def __str__(self):
#         return f"Name: \t {Person.firstName}\nSurname: {Person.lastName}\nBirth date: {Person.birthDate}\n"
#
#     def getCity(self):
#         return Person.__city
#
#     def setCity(self, city):
#         Person.__city = city
#
#     def getPassword(self):
#         return Person.__password
#
#     def setPassword(self, password):
#         Person.__city = password
#
#     def changePassword(self, password, newPassword):
#         if Person.__password == password:
#             Person.__password = newPassword
#
#     def getFirstName(self):
#         return Person.firstName
#
#     def setFirstName(self, name):
#         Person.firstName = name
#
#     def getLastName(self):
#         return Person.lastName
#
#     def setLastName(self, name):
#         Person.lastName = name
#
#     def getBirthDate(self):
#         return Person.birthDate
#
#     def setBirthDate(self, date):
#         Person.birthDate = date
#
# Stepan = Person("Stepan", "Shevchenko", "1.01.1993", "Kiev", "StepanB1939")
#
# print(Stepan)


# class Airplane:
#         engine = 4
#         engine_type = "turbo"
#         color = "blue"
#         fuel = 150
#         landing_type = "ground"
#
#         def fly(self):
#             self.fuel -= 10
#
# class Hydro_Airlplane(Airplane):
#     landing_type = "water"
#
# class Air_Airplane(Airplane):
#     def __init__(self, airplane):
#         self.mothership = airplane
#
#     landing_type = "air"
#     mothership = Airplane
#
# tu_720 = Airplane()
# tu_720.fly()
# h30 = Hydro_Airlplane()
# h30.fly()
# kamikazi = Air_Airplane(tu_720)
# kamikazi.fly()


# class Human:
#     name = ""
#     surname = ""
#     proffesion = ""
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# class Builder(Human):
#     def build(self):
#         print(self.name + " just build something")
#
# class Pilot(Human):
#     def flyTo(self):
#         print(self.name + " just fly to another place")
# class Sailor(Human):
#     def sailTo(self):
#         print(self.name + " just sail to another place")
#
# Bob = Builder("Bob", "Fatt")
# Bob.build()
# Ash = Pilot("Ash", "Troop")
# Ash.flyTo()
# Papaye = Sailor("Papaye", "the Sailor")
# Papaye.sailTo()

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import dumskaya_xpath
# import time
# url = "https://dumskaya.net/"
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
# email = 'qwejvldeglmefbvlnlerv@gmail.com'
# nick = 'qwejvldeglmefbvlnlerv'
# password = 'Sqwe874895!'
# time.sleep(3)
# main_button_enter = driver.find_element('xpath',dumskaya_xpath.main_button_enter)
# main_button_enter.click()
# time.sleep(3)
# main_button_registration = driver.find_element('xpath',dumskaya_xpath.main_button_registration)
# main_button_registration.click()
# time.sleep(3)
# reg_entry_email = driver.find_element('xpath',dumskaya_xpath.reg_entry_email)
# reg_entry_email.send_keys(email)
# time.sleep(3)
# reg_entry_nick = driver.find_element('xpath',dumskaya_xpath.reg_entry_nick)
# reg_entry_nick.send_keys(nick)
# time.sleep(3)
# reg_entry_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_password)
# reg_entry_password.send_keys(password)
# time.sleep(3)
# reg_entry_rep_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_rep_password)
# reg_entry_rep_password.send_keys(password)
# time.sleep(3)
# reg_radio_male = driver.find_element('xpath',dumskaya_xpath.reg_radio_male)
# reg_radio_male.click()
# time.sleep(3)
# reg_button_finish = driver.find_element('xpath',dumskaya_xpath.reg_button_finish)
# reg_button_finish.click()






























































































