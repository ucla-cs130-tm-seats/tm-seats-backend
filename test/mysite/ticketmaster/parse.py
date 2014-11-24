#!/usr/bin/python

import json

json_data = open('event-data/0F004CFCCA844D21/0F004CFCCA844D21.pricing.json')
data = json.load(json_data)
result = data['prices'][0]['faceValue']

print result
