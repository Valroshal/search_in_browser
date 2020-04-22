# before run go to https://myaccount.google.com/lesssecureapps and allow insecure access
from brow_acts import *


def colour(text): # define colour for pass and fail
    while text != 0:
        if text.find('Pass') == -1:
            print('page: Failed')
            st = '"red"'
            return st
        else:
            print('page: Pass')
            st = '"green"'
            return st


def mail_text_startp(browser_name, open_browser): #write result for start page for all browsers
    st1 = 'Pass'
    st2 = 'Failed'
    st3 = 'Crashed'
    if browser_name == 'FF':
        filesList = glob.glob("/Users/user/Library/Application Support/Firefox/Crash Reports/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while open_browser != 0:
                if open_browser.find('yandex.ru') == -1:
                    print('start page: Failed')
                    return st2
                else:
                    print('start page: Pass')
                    return st1
    elif browser_name == 'Chrome':
        filesList = glob.glob("/Users/user/Library/Application Support/Google/Chrome/Crashpad/pending/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while open_browser != 0:
                if open_browser.find('yandex.ru') == -1:
                    print('start page: Failed')
                    return st2
                else:
                    print('start page: Pass')
                    return st1
    else: #Safari
        filesList = glob.glob("/Users/user/Library/Logs/DiagnosticReports/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while open_browser != 0:
                if open_browser.find('yandex.ru') == -1:
                    print('start page: Failed')
                    return st2
                else:
                    print('start page: Pass')
                    return st1


def mail_text_searchp(browser_name, search_browser): #write result for search for all browsers
    st1 = 'Pass'
    st2 = 'Failed'
    st3 = 'Crashed'
    if browser_name == 'FF':
        filesList = glob.glob("/Users/user/Library/Application Support/Firefox/Crash Reports/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while search_browser != 0:
                if search_browser.find('yandex.ru') == -1:
                    print('search: Failed')
                    return st2
                else:
                    print('search: Pass')
                    return st1
    elif browser_name == 'Chrome':
        filesList = glob.glob("/Users/user/Library/Application Support/Google/Chrome/Crashpad/pending/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while search_browser != 0:
                if search_browser.find('yandex.ru') == -1:
                    print('search: Failed')
                    return st2
                else:
                    print('search: Pass')
                    return st1
    else: #safari
        filesList = glob.glob("/Users/user/Library/Logs/DiagnosticReports/*")
        a = define_crash(filesList)
        if a is not None and a == 'crash':
            print('search: crashed')
            return st3
        else:
            while search_browser != 0:
                if search_browser.find('yandex.ru') == -1:
                    print('search: Failed')
                    return st2
                else:
                    print('search: Pass')
                    return st1

#def main():
#    mail_text_searchp('Safari', search_brow('Safari'))


if __name__ == '__main__':
    main()