import requests
import json
import Config

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization':Config.f2sauthorization,
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')
def generate_sms(name,bin_id,percentage_full):
    return f"Hi {name},i am {bin_id} can you please empty me. Right now i am {percentage_full} % full."
