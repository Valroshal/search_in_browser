import glob
import os
import subprocess
import time
from utils import define_crash


def open_brow(browser_name): #check if start page is by yandex.ru
        if browser_name == 'Safari':
                cmd = """osascript -e 'property x : ""\ntell application "System Events"\ntell application "Safari"\n launch\n make new document\n delay 5\nset x to get URL of front document\n end tell\nreturn x\nend tell '"""
                os.system(cmd)
                st = str(subprocess.check_output(cmd, shell=True))
                time.sleep(5)
                cmd2 = """osascript -e 'quit app "Safari"'"""
                os.system(cmd2)
                return st

        elif browser_name == 'Chrome':
                cmd = """osascript -e 'property x : ""\ntell application "System Events"\n tell application "Google Chrome"\n set x to get URL of active tab of first window\n end tell\n return x\n end tell'"""
                os.system(cmd)
                st = str(subprocess.check_output(cmd, shell=True))
                time.sleep(5)
                return st

        else:
                cmd = """osascript -e 'tell application "System Events" to set the clipboard to "y"\nproperty x : ""\n tell application "Firefox" to launch \n repeat until application "Firefox" is running \n delay 3 \n end repeat \n if application "Firefox" is running then \n activate application "Firefox" \n delay 3\ntell application "System Events" \n keystroke "l" using command down \n delay 0.1 \n key code 8 using command down \n delay 3 \n set x to the clipboard\n end tell\ndelay 2 \n end if \n return x'"""
                os.system(cmd)
                time.sleep(17)
                st = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
                return st


def search_brow(browser_name): # make search in browser and check if it is by yandex.ru, at the end close browser
        if browser_name == 'Safari':
                #cmd = """osascript -e 'property y : ""\ntell application "Safari"\ntell application "System
                # Events"\n set Query to "text"\nactivate application "Safari"\nkeystroke Query\n key code 36\n delay 5\nend tell\nend tell\n tell application "Safari"\nset y to get URL of front document\n end tell\nreturn y'"""
                cmd = """osascript -e 'property y : ""\ntell application "Safari" to activate\n delay 2\n tell application "System Events"\n set Query to "text"\nactivate application "Safari"\nkeystroke Query\n key code 36\n delay 5\nend tell\n tell application "Safari"\nset y to get URL of front document\n end tell\nreturn y'"""
                time.sleep(3)
                os.system(cmd)
                st = str(subprocess.check_output(cmd, shell=True))
                time.sleep(12)
                cmd2 = """osascript -e 'quit app "Safari"'"""
                os.system(cmd2)
                return st
        elif browser_name == 'Chrome':
                cmd = """osascript -e 'property y : ""\ntell application "Google Chrome"\n tell application "System Events"\n set Query to "text"\n activate application "Google Chrome"\n keystroke Query\n key code 36\n delay 5\n end tell\n end tell\n tell application "Google Chrome"\n set y to get URL of active tab of first window\n end tell\n return y'"""
                os.system(cmd)
                st = str(subprocess.check_output(cmd, shell=True))
                time.sleep(5)
                cmd2 = """osascript -e 'quit app "Chrome"'"""
                os.system(cmd2)
                #os.system('pkill -f Google Chrome')
                return st
        else: #FF
                cmd = """osascript -e 'property y : ""\n tell application "Firefox" \n set Query to "text" \n activate \n delay 5 \n tell application "System Events" to keystroke "t" using command down\n delay 0.1\n tell application "System Events" \n keystroke Query \n key code 36 \n delay 2 \n key code 37 using command down\ndelay 0.1 \n key code 8 using command down\n delay 5 \n end tell\n end tell \n tell application "Firefox" \n set y to the clipboard\n delay 3 \n end tell \n return y'"""
                os.system(cmd)
                time.sleep(17)
                st = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
                cmd2 = """osascript -e 'quit app "firefox"'"""
                os.system(cmd2)
                #time.sleep(2)
                #cmd3 = """osascript -e 'tell application "System Events"\n tell application "Firefox" to activate \n key code 36\n end tell'"""
                #os.system(cmd3)
                return st


#def main():
#        open_brow('FF')
#        search_brow('FF')


#if __name__ == '__main__':
#        main()


