def find(x, A):
    """
Ищет x в A и возвращает True, если такой есть
False, если такого нет
    """
    for x in A: # цикл for - списочный
        if number == x:
            return True
    return False

def generate_permutation(N:int, M:int=-1, prefix=None): # M=N
"""
Генерация всех перестановок N чисел в M позициях,
с префиксом prefix
"""
    if M == -1: # то тогда генерируем столько же в N позициях
        M = N   # по умолчанию N чисел в N позициях
"""
сокращенный вариант:
M = N if M == -1 else M
"""                       # print(prefix, end=", ", sep="") - sep - сепаратор - вывод без пробелов
    prefix = prefix or [] # print(prefix, end=", ") - вывод в строчку через ,
    if M == 0            # если осталось сгенерировать 0
        print(prefix)    # prefix[0], prefix[1], prefix[2]
        return           # print(*prefix) * - операция встраивания. Подставляются в качестве всех параметров функции значения списка
    for number in range(1, N+1): 
        if find_in(number, prefix): # ищет число в списку
            continue
        """
        if number was in prefix: # перестановки исключающие ранее встречающееся числа
            continue # перекинет на следующую итерацию
        """
        prefix.append(number)
        generate_permutation(N, M-1, prefix) # попрежнему N чисел но позицей стало меньше
        prefix.pop() # убираем то число которое добавили prefix.append

generate_permutation(3)     # Перестановка трех чисел