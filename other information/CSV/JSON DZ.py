import json
import jpype


with open('employees.json', 'r') as json_file:
    data = json.load(json_file)

    print(type(data), data)
