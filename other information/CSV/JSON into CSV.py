import json


try:
    with open('employees.json', 'r') as json_file:
        data = json.loads(json_file.read())
    output = ','.join([*data[0]])
    print(output)
    for obj in data:
        output += f'\n{obj["name"]},{obj["birthday"]},{obj["height"]}, {obj["weight"]}, {obj["car"]}, {obj["languages"]}'
    print(output)
    with open('employees.csv', 'w') as csv_file:
        csv_file.write(output)

except Exception as ex:
    print(f"Error: {str(ex)}")

