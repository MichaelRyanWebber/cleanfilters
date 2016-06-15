import json
import csv
import os

f = open('filters_string','r')

fJSON = json.load(f)

path = os.path.expanduser('~/Desktop/mappings.csv')
csvFile = open(path, 'w+')
csvWriter = csv.writer(csvFile)


csvFile.write('Label,DefaultValueF,Sources,Read-Only,DefaultValueS\n')

# generate csv for each field and source
line = []
prefix = []
for (mapName, mapData) in fJSON.iteritems():
    prefix = [mapData['label'], mapData.get('defaultValue', '')]
    # iterate over the sources
    for src in mapData['sources']:
        line = list(prefix)
        line.append(src.get('source'))
        line.append(src.get('readOnly', 'false'))
        line.append(src.get('defaultValue', ''))
        csvWriter.writerow(line)

csvFile.close()
f.close()

#with open('new_filters_string','w') as outfile:
#    json.dump(fJSON,outfile)




