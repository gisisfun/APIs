import requests
import json


key = 'brAKupqRdkXNpkYRhy6SpPe1ErVJiAEc'
full_api_url ='https://api.psma.com.au/beta/v1/addresses?addressString=1%20bowes%20st%20phillip%20act%202606&stateTerritory=ALL&datum=GDA94&page=1&perPage=10'


headers = {
   "Authorization": key,
   "Accept": "application/json"
    }



print('url: {}:'.format(full_api_url))
print('header: {}'.format(headers))

url = requests.get(full_api_url, headers=headers)
print('requests status:',url.status_code)
print('JSON response:',url.json)

print('JSON text:',url.text)


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
##jsontext="""
##{
##  "data": [
##    {
##      "addressId": "GAACT716851937",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT716244438",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "1-15 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647705",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 2 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647706",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 3 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647707",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 4 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647708",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 5 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647709",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 6 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647710",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 7 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT717647711",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "LEVEL 8 1 BOWES PL, PHILLIP ACT 2606"
##    },
##    {
##      "addressId": "GAACT715695566",
##      "addressString": "1 bowes st phillip act 2606",
##      "formattedAddress": "SUITE 1 1 BOWES PL, PHILLIP ACT 2606"
##    }
##  ],
##  "links": {
##    "count": 21,
##    "current": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
##    "first": "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
##    "last": "/v1/addresses?datum=GDA94&page=3&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
##    "next": "/v1/addresses?datum=GDA94&page=2&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606",
##    "prev": null
##  }
##}
##"""

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
full_api_utl = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/asgsMain/'

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

address_psma_data = dict(
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
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('Address ID: {}'.format(address_psma_data['address_id']))
print('Address String: {}:'.format(address_psma_data['address_string']))
print('Formatted Address: {}'.format(address_psma_data['formatted_address']))
print('---------------------------------------')



nexturl = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/geo/'

nextjson ="""
{
  "addressId": "GAACT716851937",
  "geo": {
    "geoDatumCode": "GDA94",
    "geoFeature": "FRONTAGE CENTRE SETBACK",
    "geometry": {
      "coordinates": [
        149.08604671,
        -35.34404253
      ],
      "type": "Point"
    }
  }
}
"""

nexturl = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/localGovernmentArea/'

nextjson = """
{
  "messages": [
    {
      "code": "I0001",
      "description": "You have requested something that is not available.",
      "message": "localGovernmentArea is not available for GAACT716851937",
      "severity": "INFO"
    }
  ]
}
"""

nexturl = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/commonwealthElectorate/'
nextjson ="""
{
  "addressId": "GAACT716851937",
  "commonwealthElectorate": {
    "commElectoralName": "CANBERRA",
    "commElectoralPid": "ACT3"
  }
}
"""




nexturl = 'https://api.psma.com.au/beta/v1/addresses/GAACT716851937/buildings/?page=1&perPage=10'

nextjson = """
{
  "data": [
    {
      "buildingId": "BLDACT0000054352",
      "coverageType": "Urban",
      "links": {
        "area": "/v1/buildings/BLDACT0000054352/area/",
        "averageEaveHeight": "/v1/buildings/BLDACT0000054352/averageEaveHeight/",
        "centroid": "/v1/buildings/BLDACT0000054352/centroid/",
        "elevation": "/v1/buildings/BLDACT0000054352/elevation/",
        "estimatedLevels": "/v1/buildings/BLDACT0000054352/estimatedLevels/",
        "footprint2d": "/v1/buildings/BLDACT0000054352/footprint2d/",
        "footprint3d": "/v1/buildings/BLDACT0000054352/footprint3d/",
        "maximumRoofHeight": "/v1/buildings/BLDACT0000054352/maximumRoofHeight/",
        "roofComplexity": "/v1/buildings/BLDACT0000054352/roofComplexity/",
        "roofMaterial": "/v1/buildings/BLDACT0000054352/roofMaterial/",
        "solarPanel": "/v1/buildings/BLDACT0000054352/solarPanel/",
        "swimmingPool": "/v1/buildings/BLDACT0000054352/swimmingPool/",
        "zonings": "/v1/buildings/BLDACT0000054352/zonings/"
      },
      "relatedAddressIds": [
        "GAACT715695564",
        "GAACT715695565",
        "GAACT715695567",
        "GAACT715695566",
        "GAACT715695569",
        "GAACT715695570",
        "GAACT715695571",
        "GAACT715695563",
        "GAACT717647709",
        "GAACT715695573",
        "GAACT715695568",
        "GAACT717647708",
        "GAACT715695572",
        "GAACT715695574",
        "GAACT717647706",
        "GAACT717647711",
        "GAACT717647710",
        "GAACT716851937",
        "GAACT716244438",
        "GAACT714960649",
        "GAACT717647705",
        "GAACT717647707"
      ]
    }
  ],
  "links": {
    "count": 1,
    "current": "/v1/addresses/GAACT716851937/buildings/?page=1&perPage=10",
    "first": "/v1/addresses/GAACT716851937/buildings/?page=1&perPage=10",
    "last": "/v1/addresses/GAACT716851937/buildings/?page=1&perPage=10",
    "next": null,
    "prev": null
  }
}
"""


nexturl = 'https://api.psma.com.au/beta/v1/buildings/BLDACT0000054352/'

nextjson = """
{
  "buildingId": "BLDACT0000054352",
  "coverageType": "Urban",
  "links": {
    "area": "/v1/buildings/BLDACT0000054352/area/",
    "averageEaveHeight": "/v1/buildings/BLDACT0000054352/averageEaveHeight/",
    "centroid": "/v1/buildings/BLDACT0000054352/centroid/",
    "elevation": "/v1/buildings/BLDACT0000054352/elevation/",
    "estimatedLevels": "/v1/buildings/BLDACT0000054352/estimatedLevels/",
    "footprint2d": "/v1/buildings/BLDACT0000054352/footprint2d/",
    "footprint3d": "/v1/buildings/BLDACT0000054352/footprint3d/",
    "maximumRoofHeight": "/v1/buildings/BLDACT0000054352/maximumRoofHeight/",
    "roofComplexity": "/v1/buildings/BLDACT0000054352/roofComplexity/",
    "roofMaterial": "/v1/buildings/BLDACT0000054352/roofMaterial/",
    "solarPanel": "/v1/buildings/BLDACT0000054352/solarPanel/",
    "swimmingPool": "/v1/buildings/BLDACT0000054352/swimmingPool/",
    "zonings": "/v1/buildings/BLDACT0000054352/zonings/"
  },
  "relatedAddressIds": [
    "GAACT715695564",
    "GAACT715695565",
    "GAACT715695567",
    "GAACT715695566",
    "GAACT715695569",
    "GAACT715695570",
    "GAACT715695571",
    "GAACT715695563",
    "GAACT717647709",
    "GAACT715695573",
    "GAACT715695568",
    "GAACT717647708",
    "GAACT715695572",
    "GAACT715695574",
    "GAACT717647706",
    "GAACT717647711",
    "GAACT717647710",
    "GAACT716851937",
    "GAACT716244438",
    "GAACT714960649",
    "GAACT717647705",
    "GAACT717647707"
  ]
}
"""