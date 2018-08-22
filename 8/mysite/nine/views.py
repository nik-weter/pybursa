import csv, os
from datetime import date, datetime

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def get_discr(a, b, c):
    d = b**2 - 4*a*c
    return d


def get_eq_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x


def quad_equation(request):
    args_warning = "You must provide all three coefficients equation!"
    result_message = "Roots of the equation do not exist"
    arguments = ['a', 'b', 'c']
    context_dict = {}
    for arg in arguments:
        value = request.GET.get(arg)
        if value is not None:
            value = int(value)
            context_dict[arg] = value
        else:
            return HttpResponse(args_warning)

    a = context_dict['a']
    b = context_dict['b']
    c = context_dict['c']
    d = get_discr(a, b, c)
    if d < 0:
        return HttpResponse(result_message)
    else:
        x1 = get_eq_root(a, b, d)
        x2 = get_eq_root(a, b, d, order=2)
        if x1 == x2:
            result_message = "There is one root: x1 = x2 = %g" % x1
        else:
            result_message = "There are two roots: x1 = %g, x2 = %g" % (x1, x2)
    context_dict.update({'d': d, 'message': result_message})
    return render(request, 'nine/equations.html', context_dict)

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

def heroes(request):
    context = {}
    context['heroes'] = get_heroes('data.csv', nick=None)
    return render(request, 'nine/hero.html', context)

def get_heroes(filename, nick=None):
    with open(filename, 'r') as f:
        file = csv.DictReader(f)
        heroes_list = []
        for row in file:
            id = row['id']
            surname = row["surname"]
            name = row["name"]
            birthdate = row["birthdate"]
            nickname = row["nickname"] or None
            person = Person(id, surname, name, birthdate, nickname)
            row["fullname"] = person.fullname
            row["age"] = person.age
            if nick is not None and nickname is not None:
                if nick == nickname.lower():
                    return person
            heroes_list.append(person)
        return heroes_list

def hero(request, nick):
    context = {}
    hero_obj = get_heroes("data.csv", nick)
    context['superhero'] = hero_obj
    return render(request, 'nine/hero.html', context)

if __name__ == "__main__":
    for l in get_heroes("../data.csv", nick=None):
        print(l.nickname)