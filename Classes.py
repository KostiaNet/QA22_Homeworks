class Car:
    def __init__(self,name,year,manufacturer,volume, color, price):
        self.__model_name = name
        self.__release_year = year
        self.__car_manufacturer = manufacturer
        self.__engine_volume = volume
        self.car_color = color
        self.car_price = price

    def __str__(self):
        return f"Model name: {self.__model_name}\nRelease year: {self.__release_year}\nCar manufacturer: {self.__car_manufacturer}\n" \
               f"Engine volume: {self.__engine_volume}\nCar color: {self.car_color}\nCar price: {self.car_price}\n"

    __model_name = ""
    __release_year = 0
    __car_manufacturer = ""
    __engine_volume = 0
    car_color = ""
    car_price = 0

    def set_model_name(self,name):
        self.__model_name = name
    def set_release_year(self, year):
        self.__release_year = year
    def set_car_manufacturer(self, manufacturer):
        self.__car_manufacturer = manufacturer
    def set_engine_volume(self, volume):
        self.__engine_volume = volume
    def get_model_name(self):
        return self.__model_name
    def get_release_year(self):
        return self.__release_year
    def get_car_manufacturer(self):
        return self.__car_manufacturer
    def get_engine_volume(self):
        return self.__engine_volume


class Book:
    def __init__(self,name,year,publisher,genre, author, price):
        self.__book_name = name
        self.__release_year = year
        self.__book_publisher = publisher
        self.__book_genre = genre
        self.__book_author = author
        self.book_price = price

    def __str__(self):
        return f"Book name: {self.__book_name}\n" \
               f"Release year: {self.__release_year}\n" \
               f"Book publisher: {self.__book_publisher}\n" \
               f"Book genre: {self.__book_genre}\n" \
               f"Book author: {self.__book_author}\n" \
               f"Book price: {self.book_price}\n"

    __book_name = ""
    __release_year = 0
    __book_publisher = ""
    __book_genre = ""
    __book_author = ""
    book_price = 0

    def set_book_name(self,name):
        self.__book_name = name
    def set_release_year(self,year):
        self.__release_year = year
    def set_book_publisher(self,publisher):
        self.__book_publisher = publisher
    def set_book_genre(self,genre):
        self.__book_genre = genre
    def set_book_author(self,author):
        self.__book_author = author
    def get_book_name(self):
        return self.__book_name
    def get_release_year(self):
        return self.__release_year
    def get_book_publisher(self):
        return self.__book_publisher
    def get_book_genre(self):
        return self.__book_genre
    def get_book_author(self):
        return self.__book_author


class Stadium:
    def __init__(self,date,country,city,capacity, name):
        self.__open_date = date
        self.__stadium_country = country
        self.__stadium_city = city
        self.stadium_capacity = capacity
        self.stadium_name = name

    def __str__(self):
        return f"Open date: {self.__open_date}\n" \
               f"Stadium country: {self.__stadium_country}\n" \
               f"Stadium city: {self.__stadium_city}\n" \
               f"Stadium capacity: {self.stadium_capacity}\n" \
               f"Stadium name: {self.stadium_name}\n"

    __open_date = ""
    __stadium_country = ""
    __stadium_city = ""
    stadium_capacity = 0
    stadium_name = ""

    def set_open_date(self,date):
        self.__open_date = date
    def set_stadium_country(self, country):
        self.__stadium_country = country
    def set_stadium_city(self, city):
        self.__stadium_city = city
    def get_open_date(self):
        return self.__open_date
    def get_stadium_year(self):
        return self.__stadium_country
    def get_stadium_manufacturer(self):
        return self.__stadium_city



daevoo_lanos = Car("Daewoo Lanos",1997,"Daewoo motors",48,"black", 3500)
print(daevoo_lanos)
witcher = Book("The Witcher", 1986,"SuperNowa","Dark fantasy","Andrzej Sapkowski",120)
print(witcher)
stadium = Stadium("12.08.1923", "Ukraine", "Donetsk", 70050, "NSC \"Olimpiyskiy\"")
print(stadium)