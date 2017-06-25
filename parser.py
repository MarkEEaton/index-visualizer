import csv
import json
from copy import copy
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
        level1 = item['name']
        level2 = item['children'][0]['name']
        level3 = item['children'][0]['children'][0]
        list_of_names = [x['name'] for x in new_hier['children']] 
        if item['name'] not in list_of_names:
            new_hier['children'].append(item)
            print('adding')
        else:
            [x['children'].append({'name': level2, 'children': [level3]})\
             if level1 == x['name'] else print(level1 + ' pass')\
             for x in new_hier['children']]
            pass

    pprint(new_hier)


if __name__ == '__main__':
    rectangulate()
    hierarchify()
    deduplicate()
    amalgamate()

with open('index.json', 'w') as f2:
    json.dump(new_hier, f2)
