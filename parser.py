import csv
import json
import pandas as pd
from pprint import pprint

index = []
hier = {} 

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

#pprint(index)

for item in index:
    pages = []
    if item[2] != None:
        for row in index:
            if item[0] in row:
                if item[1] in row:
                    pages.append(row[2])
            pages = list(set(pages))
        hier[item[0]] = {item[1]: pages}
    else:
        #hier[item[0]] = item[1]
        pass

pprint(hier)


#df = pd.DataFrame(hier)
#df.set_index(['level1', 'level2'], inplace=True)
#df = df.groupby(['level1']).reset_index()
#hier = df.groupby(['level1', 'level2'])['level3'].apply(list)

"""
for item in index:
    if len(item) == 3:
        if {item[0]: {item[1]: [item[2]]}} not in hier:
            hier.append({item[0]: {item[1]: [item[2]]}})
        else:
            print('else case')
            hier[-1:].append(item[2])
#    elif len(item) == 2:
#        if item[0] not in hier:
#            hier[item[0]] = [item[1]]
#        else:
#            hier[item[0]].append(item[1])

hier = {'name': 'index',
        'children': hier}

#pprint(hier)
"""

with open('index.json', 'w') as f2:
    json.dump(hier, f2)



