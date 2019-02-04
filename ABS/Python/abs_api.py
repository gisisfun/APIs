import sqlalchemy
import requests
import json
import pandas as pd
import sqlite3

##2016
##SA2 Males	Females	Persons
##101051539	11,447	11,441	22,890	
##101051540 6,543	6,127	12,670

keyformat = '{0}:0:0:0:{1}:0'
full_api_url ='http://stat.data.abs.gov.au/sdmx-json/data/ABS_C16_T01_SA/1+3+2.TT.1.SA2./all?detail=Full&dimensionAtObservation=AllDimensions&startPeriod=2016&endPeriod=2016'
full_api_header = """ 
headers = {
'Content Type': 'application/json'
}
"""
print('url:\n {}'.format(full_api_url))
print('\n')
print('header: {}'.format(full_api_header))
url = requests.get(full_api_url)
print('requests status:\n',url.status_code)
print('\n')
print('JSON response:\n',url.json)
print('\n')
print('JSON text:\n',url.text)


raw_api_dict = json.loads(url.text)
print(raw_api_dict)

print('\n')
print('Auto method')

abs_data = dict(
    request_id = raw_api_dict.get('header').get('id'),
    request_href = raw_api_dict['header']['links'][0]['href'],
    description = raw_api_dict['structure']['description'],
    request_dim_cat_name0 = raw_api_dict['structure']['dimensions']['observation'][0]['name'],
    request_dim_value0 = raw_api_dict['structure']['dimensions']['observation'][0]['values'][0]['name'],
    request_dim_value1 = raw_api_dict['structure']['dimensions']['observation'][0]['values'][1]['name'],
    request_dim_value2 = raw_api_dict['structure']['dimensions']['observation'][0]['values'][2]['name'],
    request_filter_age_name0 = raw_api_dict['structure']['dimensions']['observation'][1]['values'][0]['name'],
    request_filter_age_id0 = raw_api_dict['structure']['dimensions']['observation'][1]['values'][0]['id'],
    request_filter_state_name1 = raw_api_dict['structure']['dimensions']['observation'][2]['values'][0]['name'],
    request_filter_state_id1 = raw_api_dict['structure']['dimensions']['observation'][2]['values'][0]['id'],
    request_filter_classification_name2 = raw_api_dict['structure']['dimensions']['observation'][3]['values'][0]['name'],
    request_filter_classification_id2 = raw_api_dict['structure']['dimensions']['observation'][3]['values'][0]['id'],
    request_filter_year_name4 = raw_api_dict['structure']['dimensions']['observation'][5]['values'][0]['name'],
    annotation_text = raw_api_dict['structure']['annotations'][0]['text']
)

print('\n')
print('Selected Data Items extracted from JSON Text String')
print('---------------------------------------')
print('Request ID: {}'.format(abs_data['request_id']))
print('Request HRef: {}:'.format(abs_data['request_href']))
print('Request observation category 0: {}'.format(abs_data['request_dim_cat_name0']))
print('Dataset description: {}:'.format(abs_data['description']))
print('Request observation filter name 0: {}'.format(abs_data['request_filter_age_name0']))
print('Request observation filter id 0: {}'.format(abs_data['request_filter_age_id0']))
print('Request observation filter name 1: {}'.format(abs_data['request_filter_state_name1']))
print('Request observation filter id 1: {}'.format(abs_data['request_filter_state_id1']))
print('Request observation filter name 2: {}'.format(abs_data['request_filter_classification_name2']))
print('Request observation filter id 2: {}'.format(abs_data['request_filter_classification_id2']))
print('Request observation filter year name 4: {}'.format(abs_data['request_filter_year_name4']))
print('Annotation Text: {}'.format(abs_data['annotation_text']))
print('---------------------------------------')

#Build dictionary items into an array
requestlist = []
requestlist.append(abs_data['request_id'])
requestlist.append(abs_data['request_href'])
requestlist.append(abs_data['request_dim_cat_name0'])
requestlist.append(abs_data['request_filter_age_name0'])
requestlist.append(abs_data['request_filter_age_id0'])
requestlist.append(abs_data['request_filter_state_name1'])
requestlist.append(abs_data['request_filter_state_id1'])
requestlist.append(abs_data['request_filter_classification_name2'])
requestlist.append(abs_data['request_filter_classification_id2'])
requestlist.append(abs_data['request_filter_year_name4'])
requestlist.append(abs_data['annotation_text'])

print('\n')
print('request response stored in an array: requestlist ')
print(requestlist)
print('\n')
print('request response stored in a dictionary: abs_data')
print(abs_data)

print('\n')
print('counting region ids')
regionidcount = len(raw_api_dict['structure']['dimensions']['observation'][4]['values'])
print('regionidcount:',regionidcount)

print('\n')
print('counting region names')
regionnamecount = len(raw_api_dict['structure']['dimensions']['observation'][4]['values'])
print('regionnamecount:',regionnamecount)

print('\n')    
print('counting headings')
headingcount = len(raw_api_dict['structure']['dimensions']['observation'][0]['values'])
print('headingcount:',headingcount)

print('\n')    
print('processing values')

print('JSON string to 2d array: matrix')
print('Init 2d array: matrix')

indexheadingcount = headingcount + 1
matrix =[[None for x in range(indexheadingcount)] for y in range(regionidcount)]

print('\n')
print('values 2d array: matrix')
print(matrix)
for y in range(regionidcount):
    for x in range(indexheadingcount):
        xneg = x - 1
        xplus = x + 1 
        yval = y - 1
        if x is 0:
            raw = raw_api_dict['structure']['dimensions']['observation'][4]['values'][y]['name']
            matrix[y][0] = raw
        else:
            key = keyformat.format(xneg,y)
            raw = raw_api_dict['dataSets'][0]['observations'][str(key)]
            matrix[y][x] = raw[0]           
        
for y in range(regionidcount):
    raw = raw_api_dict['structure']['dimensions']['observation'][4]['values'][y]['id']
    matrix[y][0:0] = [raw] 

print('\n')      
print('Matrix')        
print(matrix)        

print('\n') 
print('2d array: matrix to pandas dataframe: value_panda')

value_panda = pd.DataFrame(matrix)
value_panda.columns = ['sa2_maincode','sa2_name','males',
                     'females','total_pop']
print(value_panda.as_matrix())

conn = sqlite3.connect('test.db')
c = conn.cursor()
# Create the table of pop_sa2
#c.execute("""DROP TABLE pop_sa2""")
c.execute("""CREATE TABLE IF NOT EXISTS pop_sa2 (
            sa2_maincode INTEGER,
            sa2_name CHARACTER(30),
            males INTEGER,
            females INTEGER,
            total_pop INTEGER
            )""")
conn.commit()

test = conn.execute('SELECT * from pop_sa2')
names = [description[0] for description in test.description]
print(names)

value_panda.to_sql('pop_sa2', conn, if_exists='append', index=False)

conn.execute('SELECT * from pop_sa2').fetchall()
#>> [('SL', '8/31/2017', 81.9), ('SL', '8/31/2017', 81.9)]
