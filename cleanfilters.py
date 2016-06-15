import json

f = open('filters_string','r')

fJSON = json.load(f)

anyFilter = {
            "type": "or",
            "criteria": [
                {
                    "dataType": "*",
                    "field": "*",
                    "value": "",
                    "agent": "*",
                    "op": "not:empty"
                }
            ]
        }

# replace all filters with AnyAny
for (mapName,mapData) in fJSON.iteritems():
    mapData['filter'] = anyFilter

with open('new_filters_string','w') as outfile:
    json.dump(fJSON,outfile)




