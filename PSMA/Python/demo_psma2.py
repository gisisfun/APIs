import requests
import json


key = 'YOUR-KEY'
full_api_url ='https://api.psma.com.au/beta/v1/addresses?addressString=1%20bowes%20st%20phillip%20act%202606&stateTerritory=ALL&datum=GDA94&page=1&perPage=10'

headers = {
   "Authorization": key,
   "Accept": "application/json"
    }

print('url: {}:'.format(full_api_url))
print('header: {}'.format(headers))

#url = requests.get(full_api_url, headers=headers)
#print('requests status:',url.status_code)
#print('JSON response:',url.json)

urltext="""
{
  "data": [
    {"addressId": "GAACT716851937",
      "addressString": "1 bowes pl, phillip ACT 2606",
      "formattedAddress": "1 BOWES PL, PHILLIP ACT 2606"
    }
  ],
  "links": {
     "count": 1,
     "current": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+pl%2C+phillip+ACT+2606",
     "first": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+pl%2C+phillip+ACT+2606",
     "last": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+pl%2C+phillip+ACT+2606",
     "next": null,
     "prev": null
  }
}
"""

urltext = """
{"data": [
    {"addressId": "GAACT716851937",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "1 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT716244438",
     "addressString": "1 bowes st phillip act 2606",
     "formattedAddress": "1-15 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT717647705",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "LEVEL 2 1 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT717647706",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "LEVEL 3 1 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT717647707",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "LEVEL 4 1 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT717647708",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "LEVEL 5 1 BOWES PL, PHILLIP ACT 2606"
    },
    {"addressId": "GAACT717647709",
    "addressString": "1 bowes st phillip act 2606",
    "formattedAddress": "LEVEL 6 1 BOWES PL, PHILLIP ACT 2606"
     },
     {"addressId": "GAACT717647710",
     "addressString": "1 bowes st phillip act 2606",
     "formattedAddress": "LEVEL 7 1 BOWES PL, PHILLIP ACT 2606"
     },
     {"addressId": "GAACT717647711",
     "addressString": "1 bowes st phillip act 2606",
     "formattedAddress": "LEVEL 8 1 BOWES PL, PHILLIP ACT 2606"
     },
     {"addressId": "GAACT715695566",
     "addressString": "1 bowes st phillip act 2606",
     "formattedAddress": "SUITE 1 1 BOWES PL, PHILLIP ACT 2606"
     }
  ],
 "links": {
     "count": 21,
     "current": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
     "first": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
     "last": "/v1/addresses?datum=GDA94&page=3&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
     "next": "/v1/addresses?datum=GDA94&page=2&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
     "prev": null
     }
}
"""

##counter = 0
##addressidlist = []
##itemlist = ""
##for element in raw_api_dict['data']:
##    address_id_name = raw_api_dict['data'][counter][id]
##    if counter is 0:
##        itemlist = itemlist +  address_id_name
##    else:
##        itemlist = itemlist +  ','+ address_id_name
##    print(address_id_names)
##    regionnamelist.append(str(address_id_names))
##    counter += 1

raw_api_dict = json.loads(urltext)
print(raw_api_dict)

address_psma_data = dict(
    address_id = raw_api_dict['data'][0]['addressId'],
    address_string = raw_api_dict['data'][0]['addressString'],
    formatted_address = raw_api_dict['data'][0]['formattedAddress']
)

print('\n')
print('Selected Data Items extracted from JSON Text String')
print('---------------------------------------')
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('---------------------------------------')

addressid = address_psma_data['address_id']
full_api_url = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/asgsMain/'

print('url: {}:'.format(full_api_url))
print('header: {}'.format(headers))

##url = requests.get(full_api_url, headers=headers)
##print('requests status:',url.status_code)
##print('JSON response:',url.json)
##
##print('JSON text:',url.text)


urltext = """
{
  "addressId": "GAACT716851937",
  "asgsMain": {
    "2011": {
      "mbId": "80036983000",
      "sa1Id": "80109110909",
      "sa2Id": "801091109",
      "sa2Name": "PHILLIP",
      "sa3Id": "80109",
      "sa3Name": "WODEN",
      "sa4Id": "801",
      "sa4Name": "AUSTRALIAN CAPITAL TERRITORY"
    },
    "2016": {
      "mbId": "80036983000",
      "sa1Id": "80109110914",
      "sa2Id": "801091109",
      "sa2Name": "PHILLIP",
      "sa3Id": "80109",
      "sa3Name": "WODEN VALLEY",
      "sa4Id": "801",
      "sa4Name": "AUSTRALIAN CAPITAL TERRITORY"
    }
  }
}
"""

raw_api_dict = json.loads(urltext)
print(raw_api_dict)

asgs_psma_data = dict(
    address_id = raw_api_dict.get('addressId'),
    mesh_block_id_2011 = raw_api_dict.get('asgsMain').get('2011').get('mbId'),
    sa1_maincode_2011= raw_api_dict.get('asgsMain').get('2011').get('sa1Id'),
    sa2_maincode_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa2Id'),
    sa2_name_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa2Name'),
    sa3_code_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa3Id'),
    sa3_name_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa3Name'),
    sa4_code_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa4Id'),
    sa4_name_2011 = raw_api_dict.get('asgsMain').get('2011').get('sa4Name'),
    mesh_block_id_2016 = raw_api_dict.get('asgsMain').get('2016').get('mbId'),
    sa1_maincode_2016= raw_api_dict.get('asgsMain').get('2016').get('sa1Id'),
    sa2_maincode_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa2Id'),
    sa2_name_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa2Name'),
    sa3_code_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa3Id'),
    sa3_name_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa3Name'),
    sa4_code_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa4Id'),
    sa4_name_2016 = raw_api_dict.get('asgsMain').get('2016').get('sa4Name')
)

print('\n')
print('Selected Data Items extracted from JSON Text String')
print('---------------------------------------')
print('Address ID: {}'.format(asgs_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('2011 Mesh Block Code: {}:'.format(asgs_psma_data['mesh_block_id_2011']))
print('2011 SA 1 Maincode: {}'.format(asgs_psma_data['sa1_maincode_2011']))
print('2011 SA 2 Maincode:: {}'.format(asgs_psma_data['sa2_maincode_2011']))
print('2011 SA 2 Name: {}:'.format(asgs_psma_data['sa2_name_2011']))
print('2011 SA 3 Code:: {}'.format(asgs_psma_data['sa3_code_2011']))
print('2011 SA 3 Name: {}:'.format(asgs_psma_data['sa3_name_2011']))
print('2011 SA 4 Code:: {}'.format(asgs_psma_data['sa4_code_2011']))
print('2011 SA 4 Name: {}:'.format(asgs_psma_data['sa4_name_2011']))
print('2016 Mesh Block Code: {}:'.format(asgs_psma_data['mesh_block_id_2016']))
print('2016 SA 1 Maincode: {}'.format(asgs_psma_data['sa1_maincode_2016']))
print('2016 SA 2 Maincode:: {}'.format(asgs_psma_data['sa2_maincode_2016']))
print('2016 SA 2 Name: {}:'.format(asgs_psma_data['sa2_name_2016']))
print('2016 SA 3 Code:: {}'.format(asgs_psma_data['sa3_code_2016']))
print('2016 SA 3 Name: {}:'.format(asgs_psma_data['sa3_name_2016']))
print('2016 SA 4 Code:: {}'.format(asgs_psma_data['sa4_code_2016']))
print('2016 SA 4 Name: {}:'.format(asgs_psma_data['sa4_name_2016']))
print('---------------------------------------')
