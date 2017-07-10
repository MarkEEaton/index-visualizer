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
    """ make the data rectangular by adding none values """
    for row in index:
        if len(row) < 3:
            row.append(None)
        else:
            pass


def hierarchify():
    """ create the hierarchy for items with 3 levels"""

    # make the basic structure
    for item in index:
        hier['children'].append({'name': item[0],
                                 'children': []}) 

    deduplicate()

    for item in index:

        # add the two-level items
        if item[2] == None:
            [d['children'].append({'name': item[1], 'size': 1}) for d in hier['children'] if d['name'] == item[0] and item[2] == None]

# all good up to here...

        # add the three-level items
        if item[2] != None:
            [d['children'].append({'name': item[1], 'children': [{'name': item[2], 'size': 0}]}) for d in hier['children'] if d['name'] == item[0]]

        else:
            pass


def deduplicate():
    """ dedup hier by converting to json then making a set """
    json_check = []
    json_final = []
    
    for item in hier['children']:
        json_check.append(json.dumps(item))
    
    json_set = sorted(list(set(json_check)), key=str.lower)
    
    for item in json_set:
       json_final.append(json.loads(item))
    
    hier['children'] = json_final


def amalgamate():
    amalgamated = []

    for item in hier['children']:
        names = []
        for subitem in item['children']:
            names.append(subitem['name'])
        names = list(set(names))
        print(names)
        
        level1 = item['name']
        level2 = item['children'][0]['name']

        # replace code below with a way to sub in a unified subentry

        #for subitem in item['children']:
        #    if 
"""
        list_of_names = [x['name'] for x in new_hier['children']] 
            if item['name'] not in list_of_names:
                new_hier['children'].append(item)
            else:
                [x['children'].append({'name': level2, 'children': [level3]})\
                 if level1 == x['name'] else 100000000\
                 for x in new_hier['children']]
                pass
"""

if __name__ == '__main__':
    rectangulate()
    hierarchify()
    #amalgamate()
    #pprint(hier)

with open('index.json', 'w') as f2:
    json.dump(hier, f2)
