Check_input = input()       """ Перед включением в Init_ping - закоментить все check """
Check_IP = []
# print(M)      check       
# print(N)      check
for i in range(10):
    v = str(i)
    N.append(v)
# N = list(range(10))
# Тернарное выражение A = [ [0]* m for i in range(N)] # генератор списков -
# print(N)         # check
# type(N)          # check
count_ip_num = 0
count_octet = 0
flag = True        # Флаг выхода из цикла проверки при ошибке

""" поэлементный выбор списка вводимых значений M """
for x in Check_input:
    if flag == False:
        print("end")                 # check
        break

    elif flag == True:
        print("num=", count_ip_num)  # check
        print("Octet = ", count_octet)
        if x == ".":
            print("next IP octet")
            print(count_octet)
            count_ip_num *= 0  # reset
            count_octet += 1
            if count_octet > 3:
                print("Out of range, there can't be more than 3 octets", count_octet)  # Ошибка ввода
                flag = False
                break
            # elif count_ip_num == 3 and count_octet <= 3:  # Numbers counter XXX.ZZZ.YYY.AAA
            #   count_ip_num *= 0  # reset
            #   count_octet += 1  # Octet counter >3 "."
            #   continue  # !) Проверить необходимость
            elif count_ip_num > 3:
                print("Out of range", count_ip_num)  # Ошибка ввода
                flag = False
                break
            #  elif count_ip_num == 3:
            #       print("out of range")  # Ошибка ввода
            #       break

        elif count_ip_num <= 3:
             #   print(count_ip_num) # check
             #   print("N=", N)      # check
            for z in Check_IP:  # поэлементный выбор списка значений N = {1 - 9}
            #    print(type(z))  # check
                print('x=', x)  # check
                print('z=', z)  # check
                print("C=", count_octet)
                if (x == z) == True and count_octet <= 3:
                    print("equal")
                    count_ip_num += 1
                    break  # if x(1) = z(1) - end cycle
                elif count_ip_num == 3:
                    print("Out of range")   # Дописать почему
                    flag = False
                    break
                elif count_ip_num > 3:
                    print("IP address out of range")
                    flag = False
                    break
                else:
                    pass
                #    print(type(x))         check

        else:
            print("IP address out of range")
           # flag = False

"""
Tasks:
    1) Функционировать все повторы в def
    2) flag = false, break - выход из init цикла: проверить оптимизацию со stackoverflow:
        
        #stackoverflow
      Вопрос:
        Есть входной список, элементы которого состоят из некого текста. Нужно проверить, есть ли в элементах списка слова из одного списка и из другого, и если есть слова из одного, и нет из другого, то вывести некое сообщение.
Не получается завершить несколько циклов после получения результата и перейти к следующему элементу списка

some_text = ['some text','another text','one more']
whitelist = ['another','more']
blacklist = ['some','else']
for text in some_text:
    for items in blacklist:
        if text.find(items) != -1:
            for item in whitelist:
                if text.find(item) == -1:
                    print('Found!')
                else:
                    print('Not found')
      Ответ:
        Для выхода из цикла до его нормального завершения в Python используется оператор break:

for item in items:
    if some_condition:
        break
Для того, чтобы выйти из нескольких циклов по условию, выполнившемуся во внутреннем цикле, используется флаг выхода - переменная, которая изначально имеет значение False, а при необходимости выйти из цикла преждевременно принимает значение True:

flag = False
for outer in outer_list:
    for inner in inner_list:
        if some_condition:
            flag = True
            break
    if flag:
        break
Таким образом можно выйти из любого количества вложенных циклов, нужно лишь добавлять проверку на флаг выхода в конец каждого.

Вариант второй, красивый

Вам стоит немного поменять структуру вашего кода. Для начала вынесите проверки на вхожденения слов из blacklist и whitelist в отдельную функцию:

def contains_words(text, words_list):
    for word in words_list:
        if text.find(word) != -1:
            return True
    return False
Теперь проверка на вхождение слов из whitelist и невхождение слов из blacklist будет выглядеть так:

for text in some_text:
    if contains_words(text, whitelist) and not contains_words(text, blacklist):
        print("Found")
    else:
        print("Not found")
Если выражение contains_words(text, whitelist) вернёт False, Python не станет вычислять значение выражения not contains_words(text, blacklist), так как, каким бы оно ни было, значение выражения contains_words(text, whitelist) and not contains_words(text_blacklist) всегда будет False.

Переписав код таким образом вы сохраните изначально задуманную функциональность, при этом значительно повысив читаемость кода и упростив возможные изменения в будущем.



"""


