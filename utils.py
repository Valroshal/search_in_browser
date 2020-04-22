import datetime
import glob
import ntpath
from pathlib import Path
import os
from datetime import date
import os.path, time


def define_crash(list): # get list of crashlog files and quantity of crashes from today(from this list)
    count = 0
    crash = "crash"
    ok = "ok"
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    print(today)
    for i in list:
        file_date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(i)))
        print(file_date)
        if file_date == today:
            count += 1
    if count > 0:
        print("Num of crashes = ", count)
        return ok  # crash
    return ok


def crash_on_start(browser_name, del_path, s_list): # to check if there were crash logs for today before test and remove it

    today = datetime.datetime.today().strftime('%Y-%m-%d')

    if browser_name == 'Safari':
        count = []

        for i in s_list:
            file_date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(i)))

            if file_date == today:
                count.append(i)
        for j in count:
            name = path_leaf(j)
            cmd = 'rm -rf ' + del_path + name
            print(cmd)
            os.system(cmd)
    elif browser_name == 'Chrome':
        count = []

        for i in s_list:
            file_date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(i)))

            if file_date == today:
                count.append(i)
        for j in count:
            name = path_leaf(j)
            cmd = 'rm -rf ' + del_path + name
            print(cmd)
            os.system(cmd)
    else: #FF
        count = []

        for i in s_list:
            file_date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(i)))

            if file_date == today:
                count.append(i)
        for j in count:
            name = path_leaf(j)
            cmd = 'rm -rf ' + del_path + name
            print(cmd)
            os.system(cmd)

def path_leaf(path):   #get name of file from full path
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

