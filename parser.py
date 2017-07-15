import csv
import json
from random import random

index = []
hier = {'name': 'index',
        'children': []}
new_hier = {'name': 'index',
            'children': []}


""" create an index list, ignoring see and see also references """
with open('miller.txt', 'r') as f1:
    data = csv.reader(f1, delimiter='\t')
    for row in data:
        if row[-1:][0][0:3] != 'see':
            index.append(row)


def rectangulate():
    """ make the data rectangular by adding None values """
    for row in index:
        if len(row) < 3:
            row.append(None)
        else:
            pass


def hierarchify():
    """ create the hierarchy """

    # make the basic structure
    for item in index:
        hier['children'].append({'name': item[0],
                                 'children': []})

    deduplicate()

    for item in index:

        # add the two-level items
        if item[2] is None:
            [d['children'].append({'name': item[1], 'size': random()})
             for d in hier['children'] if d['name'] == item[0]]

        # add the three-level items
        if item[2] is not None:
            [d['children'].append({'name': item[1],
                                   'children': [{'name': item[2],
                                                 'size': random()}]})
             for d in hier['children'] if d['name'] == item[0]]

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
    """ iterate through subitems and yield the current one """
    for item in hier['children']:
        for subitem in item['children']:
            yield subitem, item


def amalgamate():
    """ set up the amalgamation """
    past_subitem = {'name': 'blah'}
    ys1 = yield_subitem()
    while True:
        create_subitem = past_subitem
        try:
            subitem, item = next(ys1)
        except StopIteration:
            return
        past_subitem = individual_amalgamate(subitem,
                                             past_subitem,
                                             create_subitem,
                                             ys1)


def individual_amalgamate(subitem, past_subitem, create_subitem, ys1):
    """ amalgamate the individual items. Recurse when needed. """
    try:
        if subitem['name'] != past_subitem['name']:
            pass
        else:
            create_subitem['children'].append(subitem['children'][0])
            past_subitem = subitem
            try:
                subitem, item = next(ys1)
            except StopIteration:
                return
            individual_amalgamate(subitem, past_subitem, create_subitem, ys1)
            subitem = create_subitem[:]
    except Exception as e:
        print('exception: ' + e)
    finally:
        past_subitem = subitem
        return past_subitem


def final_dedup():
    """ wrap it up by making a new_hier without any duplicates """
    past_subitem = {'name': 'blah'}
    to_delete = []
    for item in hier['children']:
        for subitem in item['children']:
            if past_subitem['name'] == subitem['name']:
                to_delete.append(subitem)
            else:
                pass
            past_subitem['name'] = subitem['name']
    for idx1, item in enumerate(hier['children']):
        for idx2, subitem in enumerate(item['children']):
            if subitem in to_delete:
                try:
                    test1 = hier['children'][idx1]['children'][idx2]['children']
                    hier['children'][idx1]['children'][idx2] = {}
                except:
                    pass
            else:
                pass

def clean_empty(d):
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [v for v in (clean_empty(v) for v in d) if v]
    return {k: v for k, v in ((k, clean_empty(v)) for k, v in d.items()) if v}


if __name__ == '__main__':
    rectangulate()
    hierarchify()
    amalgamate()
    final_dedup()
    hier = clean_empty(hier)

with open('index.json', 'w') as f2:
    json.dump(hier, f2)
