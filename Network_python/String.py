""" ___ТИПЫ ДАННЫХ В PYTHON___
Изменяемые:
- Списки       list()     # Список vlan; Список команд; Однотипные данные
- Словари                 # Когда нужно описать информацию про маршрутизатор; IP= ; hostname = ;
- Множества

Не изменяемые:
- Числа
- Строки       str()      # Конфиг считывает в виде строки; Отправить команду на устройство; IP записать в программе;  
- Кортежи                 # Не изменяемый список (С++ - Массив)
"""

''' Строки, можно обращаться по индексам, упорядоченный, не изменяемый тип данных
___Литералы___  
Литерал (англ. literal) — запись в исходном коде компьютерной программы, представляющая собой фиксированное значение. 
Литералами также называют представление значения некоторого типа данных.

Булевы: True, False
Символьные: 'a', '\n'
Целочисленные: 29, 0х1D # По умолчанию тип 'int'
Числа с плавающей запятой: 1., .1, 1е1, 1е-4D
Строковые: "Это строковый литерал", "" 
'''

""" Методы строк"""                 # Методы строк всегда быстрее в отличии от регулярных выражений
l = 'interface g0/0'
x = l.upper()                  | 'INTERFACE G0/0'     # Все ЗАГЛАВНЫЕ буквы  | str.upper(l)
x = l.lower()                  | 'interface g0/0'     # Все строчные буквы
x = l.capitalize()             | 'Interface g0/0'     # Заглавная первая буква
x = l.startwith('interface')   | True / False         # Строка начинается с ...
x = l.endwith('g0/0')          | True / False         # Строка заканчивается на ... | В конце может быть спец. символ
l.find('g0/0')                 | 10 - эл-нт массива   # Поиск начала строки 
l.count('0')                   | 2                    # Кол-во символов ()
len(l)                         | 14                   # '\n' - спец символы = 1 | Длина строки в символаъ
sorted('test')                 | ['e', 's', 't', 't'] # Сортировка строки
l.isdiget()                    | False                # Проверяет все ли символы - числа (int)

""" whitespace - спецсимволы """                      # \n\r\t\v\a\b\f
x = l.replace('0/0'; '1/3', 1) | 'interface g1/3'     # Замена части строки ('что', 'на что'); Если 'что' встретилось 2 раза - заменить все; 1 - какое кол-во повторов заменить                                             
l = '\tinterface g0/0\t'       | '  interface g0/0    '
l.strip()                      | 'interface g0/0'     # Убирает все спецсимволы слева и справа
l.lstrip()                     | 'interface g0/0    ' # Убирает все спецсимволы слева
l.rstrip()                     | '  interface g0/0'   # Убирает все спецсимволы справа
a = '[110/70]' | a.strip('[]') | '110/70'             # Конкретное удаление, в любом порядке; символы в самом начале и в самом конце
trunk = 'switchport trunk allowed vlan 1,2,3,4,5,7,100' # .split() - из строки делает список, избавляется от всех символов
trunk.split()  | ['switchport', 'trunk', 'allowed', 'vlan', '1,2,3,4,5,7,100'] # Разделяет строку по спейс символам (пробелам)
vlans = '1,2,3,4,5,7,100'
vlans.split(',')               | ['1', '2', '3', '4', '5', '7', '100'] # Разделение по символы (' ')

""" Форматирование строк - позволяет делать шаблоны: """ # Позволяет подставлять списки, строки, числа и тп.
intf_template = 'intetface {}' # {} - переменная значение
intf_template.format('g0/0')   | 'intetface g0/0'   # Подстановка строки
intf_template.format(g0/0)     | 'intetface g0/0'   # Подстановка числа

""" Метод .format """
template = "{} {} {}"                               # 3 - переменные
template = "3, 4, 65, 7"       | '3, 4 ,65'         # Лишнее - отбрасывает

intf = 'g0/0'
mac = 'AAAA:BBBB:CCCC'
vlan = 10
template.format(intf, vlan, mac)    | 'g0/0 10  AAAA:BBBB:CCCC' # Подстановка переменных
""" Форматирование строк """
template = "{:7} {:5} {:15}"     |  # :7 - ширина столбца
'g0/0       10 AAAA:BBBB:CCCC '

# Числа выравниваются по правой стороне, а все остальное по левой
template = "{:7} {:<5} {:15}"    |  # < - выравнивать по левой стороне
'g0/0    10    AAAA:BBBB:CCCC '

template = '''
IP address: {}
Mask:       {}
Interface   {}
'''

template.format('10.1.1.1', 24, 'Gi0/0')
'\n... IP address: 10.1.1.1\n... Mask:       24\n... Interface   Gi0/0\n... '

print(template.format('10.1.1.1', 24, 'Gi0/0'))
 #IP address: 10.1.1.1
 #Mask:       24
 #Interface   Gi0/0

# читабельный формат:
template = '''             
IP address: {IP}
Mask:       {mask}
Interface   {intf}
'''
print(template.format(IP='10.1.1.1', mask=24, intf='Gi0/0')) # IP, mask, intf - в любом порядке
#IP address: 10.1.1.1
# Mask:       24
# Interface   Gi0/0

#Дублирование {}:
template = '''
Information {IP}/{mask}         
IP address: {IP}
Mask:       {mask}
'''
print(template.format(IP='10.1.1.1', mask=24))
#Information 10.1.1.1/24         
#IP address: 10.1.1.1
#Mask:       24

""" Конвертирование IP в двоичный формат """
'{:b}'.format(255)  | '11111111'                  # Конвертирует число 

'{:b}.{:b}.{:b}.{:b}'.format(192,168,1,1)
'11000000.10101000.1.1'

'{:08b}.{:08b}.{:08b}.{:08b}'.format(192,168,1,1) # :08 - добавить нули до 8 символов
'11000000.10101000.00000001.00000001'


