#!/usr/bin/python
import subprocess
import os
count = 0			# count octet numbers - 1.2.3.{1-254}
IP_b = []			# list - 'negativ' .4octet_IP
IP_b_str = '' 			# collecting list in a row
print("Enter your IP-adress")
IP_address = input()
IP_address = list(IP_address)   # conversion input IP-address in the string

pwd_ad = os.popen("pwd").read() # find path ./
pwd_row = ''
pwd_row = pwd_row + pwd_ad
touch_cmd = subprocess.run(["touch", pwd_row, "ping_broadcast.log"]) #create log

# futere check input address

for i in range(0, len(IP_address)):
    if IP_address[i] == ".":	    # counting octet IP-address
       count += 1
       IP_b.append(IP_address[i])   # collecting input IP numbers in the row
    elif count == 3:
         break
    else:
       IP_b.append(IP_address[i])

full_oct3 = IP_b_str.join(IP_b)     # full inputIP-adress - 'negativ' .4octet_IP

list_count = ''
myfile=open('ping_broadcast.log', 'w')
for i in range(1, 3):
    list_count = list_count + str(i)
    End_IP = full_oct3 + list_count		# type:row
    bash_cmd = subprocess.run(["ping", End_IP, "-c 2", "-i 0.3"], stdout=subprocess.DEVNULL)
#    print(bash_cmd)  check
    list_count = ''
    if  bash_cmd.returncode == 0:		# error cycle
        host_up = print(End_IP, "host up")
        print>>myfile, elements
    elif bash_cmd.returncode == 1:
        host_down = print(End_IP, "host down")


#    with open('ping_broadcast.log') as out:
#      subprocess.call([host_up, host_down], stdout=out)
