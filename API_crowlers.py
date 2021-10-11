import json
import requests
import time
from IPython.core.display import clear_output

import requests_cache

requests_cache.install_cache()


def get_web(payload):

    header={
        'user-agent': 'XXXXXXXXX'
        }
    url='https://ws.audioscrobbler.com/2.0/'
    response=requests.get(url, headers=header, params=payload)


    return response


initial_pg=1
total_pg=99999

result=[]

while initial_pg<=total_pg:

    payload = {
    'api_key': '************************',
    'method': 'chart.gettopartists',
    'format': 'json',
    'limit': 500,
    'page': initial_pg
      }

    
    print("requested page {}/{}".format(initial_pg,total_pg))
    clear_output(wait=True)

    #to get api data
    response=get_web(payload)

    if response.status_code !=200:
        print(response.text)
        break



    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    result.append(response)


    if not getattr(response,'from cache', False):
        time.sleep(0.25)


    initial_pg += 1