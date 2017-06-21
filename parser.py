import csv
import json
from pprint import pprint

index = []
hier = {'name': 'index',
        'children': []} 
new_hier = {'name': 'index',
            'children': []} 


with open('miller.txt', 'r') as f1:
    data = csv.reader(f1, delimiter='\t')
    for row in data:
        if row[-1:][0][0:3] != 'see':
            index.append(row)


def rectangulate():
    for row in index:
        if len(row) < 3:
            row.append(None)
        else:
            pass


def hierarchify():
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

def deduplicate():
    json_check = []
    json_final = []
    
    for item in hier['children']:
        json_check.append(json.dumps(item))
    
    json_set = sorted(list(set(json_check)), key=str.lower)
    
    for item in json_set:
       json_final.append(json.loads(item))
    
    hier['children'] = json_final

def amalgamate():
    names = []
    amalgamated = []

    for item in hier['children']:
        names.append(item['name'])
    names = list(set(names))
    for item in hier['children']:
        page = item['children'][0]['children'][0]
        for name in names:
            if item['name'] == name:
                if name not in [x['name'] for x in new_hier['children']]:
                    new_hier['children'].append(item)
                else:
                    new_hier['children'][0]\
                            ['children'][0]\
                            ['children'].append(page)
                    pass
    pprint(new_hier)

if __name__ == '__main__':
    rectangulate()
    hierarchify()
    deduplicate()
    amalgamate()

with open('index.json', 'w') as f2:
    json.dump(new_hier, f2)
