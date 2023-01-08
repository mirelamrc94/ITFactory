'12.05.2022'
'12/05/2022'
'12-05-2022'
'05-12-2022'

import datetime

d = {
    'marca': 'volvo',
    'model': 'x50',
    'an' : 2020
}

d['color'] = 'blue'
d['an'] = 2021

d['traits'] = ['200hp', '250Nm','0-100: 7s']

print(d)
print(len(d))
print(d.keys())
