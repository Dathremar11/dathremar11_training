""" Исключения """
"""
Обработка исключительных ситуаций или обработка исключений - механизм языков программирования,предназначенный для описания реакции программы 
на ошибки времени выполнения и другие возможные проблемы (исключения), которые могут возникнуть при выполнении программы и приводят к невозможности
дальнейшей отработки промраммой ее базового алгоритма

Некоторые классические примеры исключительных ситуаций:
- Деление на ноль
- Ошибка при попытке считать внешние данные
- Исчерпание допустимой памяти
Используется не только для описания ошибок и реакции на ошибки, но и для описания обработки и реакции на исключения
"""
"""
- Python автоматически генерирует исключения при возникновении ошибки времени выполнения, исключение происходит во время исполнения кода с точки зрения среды исполнения
- Код на Python может сгенерировать исключение при помощи ключевого слова raise.  # Сами создаем исключение
После него указывается объект исключения. Также можно указать класс исключения, в таком случае будет автоматически вызван конструктор без параметров. 
raise может выбрасывать в качестве исключений только экземпляры класса BaseExeprion и его наследников.
- Все стандартные классы исключений в Python являются классами нового типа (py.2 - old) и наследуются от Exception либо напрямую от BaseException. 
Все пользовательские исключения должны быть наследниками Exeption.
Все автоматически выбрасываемые исключение (пример TypeError) - это классы
"""
"""
Для того, чтобы можно было выкинуть исключение нужно создать объект исключения. Любой класс иссключения принимает в качестве параметров контруктора
дополнения (информация), которая может храниться в объекте исключения, как правила это просто исключения об ошибке.
"""
try:                  # ОБласть действия обработчика
    ...
except Exception1:    # Обработчик исключений Exception1    # Блоки, которые перехватывают исключения и описывают действия по реагированию на данное исключение
    ...
except Exception2:    # Обработчик исключений Exception2
    ...
except:               # Стандартный обработчик исключений   # Описывает реакцию на все иссключения, которые только могли возникнуть, перехватывает любое исключение
    ...               # Стандартный обработчик исключений
else:
    ...               # Код, который выполняется, если никакое исключение не возникло   # else может и не быть // если блок выполнился без ошибок
finally:              # Код, который выполняется в любом случае
    ...               # вне зависимости от того возникло исключение или нет

"""
            Блок try
Задает область действия обработчика исключений. Если при выполнении операторов в даном блоке было выброшено исключение, их выполнение
прерывается и управление переходит к одному из обработчиков. Если не возникло никакого исключения, блоки except пропускаются

"""
            
class Myobject:
    def__del___(self):
    print(self, 'is about to deleted')     # Выводит информацию на экран, что такой то объект будет сейчас удален
    obj = Myobject()
    def obj  # Python имеет автоматическое управление памятью, мы не можем сказать ему когда нужно удалить какой то объект. Объект не удалиться.
    # Все объекты, которые создаются динамически (В Python-это все объекты, т.к. все типы данных являются ссылочными)
    # размещаются в специальной области памяти, которая называется heap (куча). Любая переменная - это ссылка на объект в heap.
    # obj = Myobject
    # id(obj)
    # 1812312388982
    # На самом деле переменная obj - это число, адрес памяти (ссылка)
    # Для любого объекта, который создается, интерпретатором ведется подсчет ссылок
    # Пока переменные указывают на объект - объект живет, если ссылок не сталось, то сборщик мусора его удаляет

    # __del__ - вызом метода удаления атрибута из объекта
    # del a, - удаление переменной a

    class ObjectWithDestructor:
        def __del__(self):
            raise Exception
        

