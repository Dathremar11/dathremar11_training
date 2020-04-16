def find(number, A):
"""
ищет number в А и возвращает True, если такой есть
False, если такого нет
"""
    for x in A:
    if number == x:
        return True
return False

""" and """

flag = False
for x in A:
    if number == x:
        flaf = True
        break
return flag



