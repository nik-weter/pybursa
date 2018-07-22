# -*- utf8 -*-
from datetime import date, datetime

class Person():
    """
    This class must get 3 atribute - surname, firstname, bitrh date - and ca get aslo nickname (defaultis None)
    Birth date must be sting in format YY-MM-DD

    See datetime docs
    """
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format =  '%Y-%m-%d'
            self.birth_date = datetime.strptime(birth_date, date_format).date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_fullname(self):
        return self.surname + " " + self.first_name

    def get_age(self):

        today = date.today()
        res = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return str(res)

if __name__ == "__main__":
    nik = Person("savelev", "nik", "1985-03-20")
    print(nik.get_age())
