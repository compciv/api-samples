"""
Documentation: https://status.github.com/api

Real-world usage: https://status.github.com/messages
"""

import json
import requests

API_ENDPOINT = 'https://status.github.com/api/messages.json'

def fetch():
    resp = requests.get(API_ENDPOINT)
    return resp.text


if __name__ == '__main__':
    txt = fetch()
    # dump data in a pretty format
    data = json.loads(txt)
    print(json.dumps(data, indent=2))

