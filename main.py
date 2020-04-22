from send_mail import *
from brow_acts import *
from slack_acts import *
from utils import *


def main():

    ff_list = glob.glob("/Users/user/Library/Application Support/Firefox/Crash Reports/*")
    ch_list = glob.glob("/Users/user/Library/Application Support/Google/Chrome/Crashpad/pending/*")
    sf_list = glob.glob("/Users/user/Library/Logs/DiagnosticReports/*")
    ff_del_path = "/Users/user/Library/Application\ Support/Firefox/Crash\ Reports/"
    ch_del_path = "/Users/user/Library/Application\ Support/Google/Chrome/Crashpad/pending/"
    sf_del_path = "/Users/user/Library/Logs/DiagnosticReports/"
    a = crash_on_start("Safari", sf_del_path, sf_list)
    b = crash_on_start("Chrome", ch_del_path, ch_list)
    c = crash_on_start("FF", ff_del_path, ff_list)
    print("Safari", a)
    print("CH", b)
    print("FF", c)


    res_safari_open = mail_text_startp('Safari', open_brow('Safari'))
    res_safari_search = mail_text_searchp('Safari', search_brow('Safari'))
    res_ch_open = mail_text_startp('Chrome', open_brow('Chrome'))
    res_ch_search = mail_text_searchp('Chrome', search_brow('Chrome'))
    res_ff_open = mail_text_startp('FF', open_brow('FF'))
    res_ff_search = mail_text_searchp('FF', search_brow('FF'))

    arr = [res_safari_open, res_safari_search, res_ch_open, res_ch_search, res_ff_open, res_ff_search] # results from open browser and search in browsers

    res = create_arr(arr) # colors' array
    slack(arr, res)


if __name__ == '__main__':
    main()
