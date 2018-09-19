from datetime import date


class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name  = last_name
        self.birth_date = birth_date
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def age(self):
        today = date.today().timetuple().tm_yday
        bDay  = self.birth_date.timetuple().tm_yday
        return (date.today().year - self.birth_date.year) - int(today < bDay)

class Female(Person):
    def __init__(self, first_name, last_name, birthd):
        super().__init__(first_name, last_name, birthd)
        print(self.birth_date)
    def age(self):
        return min(20, super().age())

# kana = Female("Gob", "Smoked", date(1995,5,28))
# print( kana.full_name())
# print( kana.age())
# kala = Female("Gob", "Smoked", date(1998,12,12))
# print( kala.full_name())
# print( kala.age())

# kana = Person("Gob", "Smoked", date(1995,5,28))
# print( kana.full_name())
# print( kana.age())
# kana = Person("Gob", "Smoked", date(1998,12,12))
# print( kana.full_name())
# print( kana.age())
