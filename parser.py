import csv
import json
from pprint import pprint

index = []
dedup = []
hier = {'name': 'index',
        'children': []} 

with open('miller.txt', 'r') as f1:
    data = csv.reader(f1, delimiter='\t')
    for row in data:
        if row[-1:][0][0:3] != 'see':
            index.append(row)

for row in index:
    if len(row) < 3:
        row.append(None)
    else:
        pass


for item in index:
    pages = []
    if item[2] != None:
        for row in index:
            if item[0] in row:
                if item[1] in row:
                    pages.append(row[2])
            pages = sorted(list(set(pages)))
        hier['children'].append({'name': item[0],
                                 'children': []}) 
        hier['children'][-1]['children'].append({'name': item[1],
                                                 'children': []})
        for page in pages:
            hier['children'][-1]\
                ['children'][-1]\
                ['children'].append({'name': page, 'size': 1})

    else:
        pass

json_check = []
json_final = []

for item in hier['children']:
    json_check.append(json.dumps(item))

json_set = sorted(list(set(json_check)))

for item in json_set:
   json_final.append(json.loads(item))

hier['children'] = json_final


with open('index.json', 'w') as f2:
    json.dump(hier, f2)
