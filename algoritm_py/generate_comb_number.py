""" Генерация комбинаторных объектов """
def gen_bin(M, prefix=" "):
    if M == 0: 
        return 
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)  


def generate_number(N:int, M:int, prefix=none):
"""
Генерирует все числа (с лидирующими нещначащами нулями) в N-ричной
системе счисления (N <= 10) длины M
"""
prefix = prefix or []
 if M == 0:  # Если больше ничего генерировать не надо, то выйти (машка)
    print(prefix)
    return
for degit in range(N):   # для цифры в диапазоне допустимых цифр от 0 до N - 1
    prefix.append(degit) # удлиняется префекс цифрой digit, которой собирается продолжать на данной итерации
    generate_number(N, M-1, prefix)
    prefix.pop()         # prefix вычитаем цифру, которую приклеили для генерации

"""
def gen_bin(M, prefix=" "):
    if M == 0: # в двоичной системе счисления / поиск мышки
        print(prefix)   
    else:   # Если не мышка, позвать двух бабок
        gen_bin(M-1, prefix+"0")  
        gen_bin(M-1, prefix+"1") # дедка зовет вторую бабку :)

"""