import csv
import json
import pandas as pd
from pprint import pprint

index = []
hier = [] 

with open('miller.txt', 'r') as f1:
    data = csv.reader(f1, delimiter='\t')
    for row in data:
        if row[-1:][0][0:3] != 'see':
            index.append(row)

for item in index:
    if len(item) == 3:
        if {item[0]: [item[1]]} not in hier:
            hier.append({item[0]: [item[1]]})
        else:
            hier[-1:].append(item[1])
#    elif len(item) == 2:
#        if item[0] not in hier:
#            hier[item[0]] = [item[1]]
#        else:
#            hier[item[0]].append(item[1])

hier = {'name': 'index',
        'children': hier}

pprint(hier)

with open('index.json', 'w') as f2:
    json.dump(hier, f2)

"""
df = pd.DataFrame(index)
df.columns = ['level1', 'level2', 'level3']
df.groupby('level2')
print(df)
"""
