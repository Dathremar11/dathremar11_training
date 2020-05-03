class Person:
    def __init__(self, name, age):         # self - ссылка на экземпляр текущего класса
            self.name = name       # автоматически вызывается после создания класса
            self.age = age
            
    def print_info(self):       # self - первый параметр любой функции атрибута который описывает метод это и есть ссылка на экземпляр текущего класса
        print(self.name, "is", self.age)

john = Person("John", 22)
lucy = Person("Lucy", 21)

"""
john = Person()     # john - Экземпляр класса
john.name = "John"  # Атрибуты даных создаются при первом обращении к ним, при первом присвоении им значения
john.age = 22       # .name - атрибут данных

lucy = Person()
lucy.name = "Lucy"
lucy.age = 21
#Обращаемся напрямую к методу данного объекта
john.print_info()   # Обращаемся напрямую к методу конкретного объекта
lucy.print_info()   # И он автоматичеки вызовет функцию атрибут, передавая
# в качестве первого аргумента тот объект, к которому привязан данный метод 
"""
"""
Повторяющиеся действия/значения заносим в функции
print(john.name, "is", john.age)
print(lucy.name, "is", lucy.age)
"""
""" Тоже самое что и:
Вызываем как обычную функцию находящуюся в классе Person
Person.print_info(john)
Person.print_info(lucy)
"""
