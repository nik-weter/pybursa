# -*- coding: utf8 -*-

import csv, os
from datetime import date, datetime

class Person:
    #def __init__(self, args, nickname=None):
    def __init__(self, id, surname, name, birthdate, nickname=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.fullname = self.surname + " " + self.name
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = '%Y-%m-%d'
            self.birthdate = datetime.strptime(birthdate, date_format).date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")
        self.age = self.get_age()

    def get_age(self):

        today = date.today()
        res = today.year - self.birthdate.year - (
        (today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return str(res)


def modifier(filename):
    with open("data.csv", "r") as csvfile:
        file = csv.DictReader(csvfile)
        with open("temp", "w", newline='') as new:
            fieldnames = ['id', 'surname', 'name', 'fullname', 'birthdate', 'nickname', 'age']
            writer = csv.DictWriter(new, fieldnames=fieldnames)
            writer.writeheader()
            for row in file:
                id = row["id"]
                surname = row["surname"]
                name = row["name"]
                birthdate = row["birthdate"]
                nickname = row["nickname"] or None
                person = Person(id, surname, name, birthdate, nickname)
                row["fullname"] = person.fullname
                row["age"] = person.age
                #writer.writerow({'id': person.id, "surname": person.surname, "name": person.name, "fullname": person.fullname,
                #                "birthdate": person.birthdate, "nickname": nickname, "age": person.age})
                writer.writerow(row)
    os.remove(filename)
    os.rename("temp", filename)

if __name__ == "__main__":
    #man = Person("Wayne", "Bruce", "1939-01-30", "Batman")
    #print(man.age)
    modifier("data.csv")