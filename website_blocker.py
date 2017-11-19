import os
import time
from datetime import datetime as dt
from sys import platform

clear = lambda: os.system('cls')

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"

if platform in ("linux", "linux2" ,"darwin"):
    hosts_path="/etc/hosts"

redirect="127.0.0.1"
website_list=open("blacklist.txt", "r").read().splitlines()

def init():
    try:
        #clear()
        print("Enter starting time (HH:MM): ")
        start_time=time_string_conversion(input().split(":"))
        print("Enter ending time (HH:MM): ")
        ending_time=time_string_conversion(input().split(":"))
        print(start_time)
        print(ending_time)
        clear()
        the_loop(start_time, ending_time)
    except ValueError:
        clear()
        print("Please enter valid inputs")
        time.sleep(2)
        init()

def time_string_conversion(string_list):
    return_list=[]
    for string in string_list:
        if string[0] == "0" and string[1] == "0":
            return_list.append("0")
        elif string[0] == "0":
             return_list.append(string[1])
        else:
            return_list.append(string)
    return return_list

def the_loop(start, end):
    print("RUNNING")
    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day,int(start[0]),int(start[1])) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,int(end[0]),int(end[1])):
            with open(hosts_path, 'r+') as file:
                content=file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
        else:
            print("LOL")
        time.sleep(5)

init()
