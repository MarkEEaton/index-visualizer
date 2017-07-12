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


def yield_subitem():
    for item in hier['children']:
        for subitem in item['children']:
            yield subitem


def amalgamate():
    past_subitem = {'name': 'blah'}
    ys = yield_subitem()
    while True:
        create_subitem = past_subitem
        subitem = next(ys)
        past_subitem = individual_amalgamate(subitem, past_subitem, create_subitem)


def individual_amalgamate(subitem, past_subitem, create_subitem):
    try:
        if subitem['name'] != past_subitem['name']:
            pass
        else:
            create_subitem['children'].append(subitem['children'][0])
            past_subitem = subitem
            print(create_subitem)
    except Exception as e:
        print(e)
    finally:
        past_subitem = subitem
        return past_subitem


if __name__ == '__main__':
    rectangulate()
    hierarchify()
    amalgamate()
    #pprint(hier)

with open('index.json', 'w') as f2:
    json.dump(hier, f2)
