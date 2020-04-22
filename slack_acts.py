import requests
import json
from brow_acts import *
from send_mail import *


def create_arr(arr_of_acts): # return array of colors for each action

    arr_of_color = [None]*6
    print('arr', arr_of_acts)
    print('color', arr_of_color)
    j = 0
    while j < len(arr_of_color):
        for i in arr_of_acts:
            if i == 'Pass':
                arr_of_color[j] = '#7CD197'
            else:
                arr_of_color[j] = '#FF0000'
            j += 1

    print('color', arr_of_color)
    return arr_of_color


def slack(arr_of_acts, arr_of_color): # send message to slack

    webhook_url = 'https://hooks.slack.com/id***'

    slack_data = {
        'attachments': [
            {
                'text': '*Test results for Safari*\n'
            },
            {
                'color': arr_of_color[0],
                'text': 'start page: ' + arr_of_acts[0]
            },
            {
                'color': arr_of_color[1],
                'text': 'default search: ' + arr_of_acts[1]
            },
            {
                'text': '*Test results for Chrome*\n'
            },
            {
                'color': arr_of_color[2],
                'text': 'start page: ' + arr_of_acts[2]
            },
            {
                'color': arr_of_color[3],
                'text': 'default search: ' + arr_of_acts[3]
            },
            {
                'text': '*Test results for Firefox*\n'
            },
            {
                'color': arr_of_color[4],
                'text': 'start page: ' + arr_of_acts[4]
            },
            {
                'color': arr_of_color[5],
                'text': 'default search: ' + arr_of_acts[5]
            }
        ]
    }

    response = requests.post(webhook_url, data=json.dumps(slack_data).encode('utf8'))

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    print(response.status_code)


