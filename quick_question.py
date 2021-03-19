# Uses the Wolfram Alpha Short Answers API to get short textual answers quickly

import requests


def ask(q_string):
    base_url = "http://api.wolframalpha.com/v1/result?"
    appid = "W7UJPV-GL2Q5JAQ8T"
    formatted_question = q_string.replace(" ", "+")
    complete_url = base_url+"i="+formatted_question+"%3F&appid="+appid
    response = requests.get(complete_url)
    return response.text
