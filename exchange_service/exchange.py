import json
import time
import urllib.request

from exchange_service import config

# Temporary storage for unloading backend rate server
rate_buffer = {}


def get_rate(url):
    try:
        response = urllib.request.urlopen(url)
        rate = json.loads(response.read())['Valute']['USD']['Value']
    except:
        return None
    return {'USD': rate}


def exchange(amount, cur_from='USD', cur_to='RUB', conf=config.Config):
    rate = {}
    global rate_buffer

    if not isinstance(amount, (int, float)):
        return None

    if not rate_buffer or (time.time() - rate_buffer['time']) > conf.RATE_TIMEOUT:
        rate = get_rate(conf.RATE_API_URL)
        if not isinstance(rate, dict) or 'USD' not in rate:
            return None
        rate_buffer = {'time': time.time(), 'rate': rate}
    else:
        rate = rate_buffer['rate']

    if cur_from == 'USD':
        return round(amount * rate['USD'], 2)
    elif cur_from == 'RUB':
        return round(amount / rate['USD'], 2)
    else:
        return None
