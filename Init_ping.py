#!/usr/bin/python
import subprocess  """ Проработать при конвертации в .exe сбор не всего содержимого библиотек (страдает размер файла) """
import os
count = 0			# count octet numbers - 1.2.3.{1-254}
IP_b = []			# list - 'negativ' .4octet_IP
IP_b_str = '' 			# collecting list in a row
print("Enter your IP-adress")
IP_address = input()    # Ввод IP-адреса
IP_address = list(IP_address)   # conversion input IP-address in the string

""" Futere choice option:
        1) broadcast ping xxx.zzz.yyy.{1-254};
        2) background process ping & > file.txt | nohup (сбор статистики)
            конвертировать bash script в .py
            # + вывод в файл.log
            # + процесс должен работать при перезагрузки ОС
            # + процесс должен работать в фоновом режиме
            # + вывод даты | пинг 
            # выбрать:
                 сортировку по seq, время sleep (интервал)
                 посмотреть загрузку цп, объема файла с библиотеками в .exe
        3) Сделать с ввода IP-адреса >> в /etc/network/networks
            # выбор опции алиас/основной
            # маска
"""

""" create file.log if /pwd """
pwd_ad = os.popen("pwd").read() # find path ./
pwd_row = ''
pwd_row = pwd_row + pwd_ad
touch_cmd = subprocess.run(["touch", pwd_row, "ping_broadcast.log"]) #create log

# futere check input address
    check_input.py



for i in range(0, len(IP_address)): """ Отрезаем 192.168.1.CUT """
    if IP_address[i] == ".":	    # counting octet IP-address
       count += 1
       IP_b.append(IP_address[i])   # collecting input IP numbers in the row
    elif count == 3:
         break
    else:
       IP_b.append(IP_address[i])

full_oct3 = IP_b_str.join(IP_b)     # full inputIP-adress - 'negativ' .4octet_IP
                                    """ список в строку """
list_count = ''                         # type:str - row = ' '
myfile=open('ping_broadcast.log', 'w')
for i in range(1, 255):                  """ 192.168.1.{1-254} - broadcast  """
    list_count = list_count + str(i)
    End_IP = full_oct3 + list_count		# type:str - row = ' '
    bash_cmd = subprocess.run(["ping", End_IP, "-c 2", "-i 0.3"], stdout=subprocess.DEVNULL)
""" 
    1) Библиотека OS, команда:
    os.system("ping 192.168.1.1 -c 5 -i 0,02 1>> text.txt")
        # - проверить записывается или перезаписывается ли в файл
        # -  нельзя подставлять переменные во внутрь команды " "
        # + выполняется ключ -i - скрорость отправки пакетов пинга
        # + 1> - вывод команды в файл, без вывода в строку
            * stdin(0) - ввод
              stout(1) - вывод
              stderr(2) - вывод ошибок
              tree - вывод в файл и в консоль
              xargs - построчно передать на ввод команде
    2) Библиотека subprocess, команда:
    bash_cmd = subprocess.run(["ping", End_IP, "-c 2", "-i 0.3"], stdout=subprocess.DEVNULL)
        # - не выполняется ключ -i - скрорость отправки пакетов пинга
        # - нельзя подставлять в больше двух переменных во внутрь команды
        # +- stdout=subprocess.DEVNULL - вывод команды отправляет в NULL, 
        но строчный отчет о выполнении кидает в консоль (0);(1)
    3) Поиск других библиотек pinging; ipaddr
 """
#    print(bash_cmd)  check   
    list_count = ''         """ вывод информации по 0/1, без статистики пинга, т.к. от команды требуется узнать только доступность хоста"""
    if  bash_cmd.returncode == 0:		# error cycle
        host_up = print(End_IP, "host up")
        print>>myfile, elements
    elif bash_cmd.returncode == 1:
        host_down = print(End_IP, "host down")  # negative save
        
""" add returnCode sort nl № N in line \n """

#    with open('ping_broadcast.log') as out:
#      subprocess.call([host_up, host_down], stdout=out)
