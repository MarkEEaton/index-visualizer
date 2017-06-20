import csv
import json
import pandas as pd
from collections import defaultdict
from pprint import pprint

index = []
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
            pages = list(set(pages))
        hier['children'].append({'name': item[0],
                                 'children': []}) 
        hier['children'][-1]['children'].append({'name': item[1],
                                             'children': []})
        hier['children'][-1]['children'][-1]['children'].append({'name': ', '.join(pages)})
    else:
        print('passing')
        pass 

pprint(hier)

with open('index.json', 'w') as f2:
    json.dump(hier, f2)



