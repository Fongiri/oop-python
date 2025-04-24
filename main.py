# Assignment 1: Design Your Own Class

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def describe(self):
        return f"{self.title} by {self.author}, published in {self.year}, Genre: {self.genre}"

    def is_classic(self):
        return self.year < 2000


# Inheritance Example
class ComicBook(Book):
    def __init__(self, title, author, year, genre, hero):
        super().__init__(title, author, year, genre)
        self.hero = hero

    def describe(self):
        return f"{self.title} (Comic) featuring {self.hero}, by {self.author}, Genre: {self.genre}"


# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # Abstract method


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


# Demonstration
if __name__ == "__main__":
    # Assignment 1
    my_book = Book("1984", "George Orwell", 1949, "Dystopian")
    print(my_book.describe())
    print("Classic:", my_book.is_classic())

    my_comic = ComicBook("Spider-Man", "Stan Lee", 1962, "Superhero", "Spider-Man")
    print(my_comic.describe())

    # Activity 2
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
