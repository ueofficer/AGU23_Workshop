import requests
import json
import pandas as pd

url = 'https://data.oceannetworks.ca/api/locations'
parameters = {'method': 'get',
              'token': '7cc08ace-86d7-4136-9dcd-dd73017d35ae'}  # replace YOUR_TOKEN_HERE
response = requests.get(url, params=parameters)

if response.ok:
    locations = json.loads(str(response.content, 'utf-8'))  # convert the json response to an object
    df = pd.json_normalize(locations)
    print(df)


else:
    if response.status_code == 400:
        error = json.loads(str(response.content, 'utf-8'))
        print(error)  # json response contains a list of errors, with an errorMessage and parameter
    else:
        print('Error {} - {}'.format(response.status_code, response.reason))
