import requests

full_api_url ='https://api.psma.com.au/beta/v1/addresses?addressString=1%20bowes%20pl%2C%20phillip%20ACT%202606&stateTerritory=ALL&datum=GDA94&page=1&perPage=10'
full_api_header = """ 
headers = {
'Content Type': 'application/json', 

'Authorization': 'brAKupqRdkXNpkYRhy6SpPe1ErVJiAEc'
}
"""
print('url: {}:'.format(full_api_url))
print('header: {}'.format(full_api_header))

url = requests.get(full_api_url, bytes(full_api_header,'utf-8'))
print('requests status:',url.status_code)
print('JSON response:',url.json)
