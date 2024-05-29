import csv
import json


# try:
#     with open('employees.json', 'r') as json_file:
#         data = json.loads(json_file.read())
#     output = ','.join([*data[0]])
#     print(output)
#     for obj in data:
#         output += f'\n{obj["name"]},{obj["birthday"]},{obj["height"]}, {obj["weight"]}, {obj["car"]}, {obj["languages"]}'
#     print(output)
#     with open('employees.csv', 'w') as csv_file:
#         csv_file.write(output)
# except Exception as ex:
#     print(f"Error: {str(ex)}")


# one_data = {
#     'name': 'Tanya Pestunova',
#     'birthday': '02.05.1991',
#     'height': 175,
#     'weight': 52,
#     'car': 'true',
#     'languages': 'null'
# }
#
# try:
#     with open('employees.json', 'r') as new_json:
#         some_open = json.load(new_json)
# except FileNotFoundError:
#
#     some_open = []
#
# some_open.append(one_data)
#
# try:
#     with open('employees.json', 'w') as into_json:
#         json.dump(some_open, into_json, indent=4)
# except Exception as ex:
#     print(f"Error: {str(ex)}")

# second_data = {
#     'name': 'Pasha Pestunov',
#     'birthday': '26.12.1997',
#     'height': 183,
#     'weight': 75,
#     'car': 'true',
#     'languages': 'python'
# }
#
# filename = 'employees.csv'
#
# fieldnames = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
#
# try:
#     file_exists = False
#     try:
#         with open(filename, 'r', newline='') as csv_file:
#             file_exists = True
#     except FileNotFoundError:
#         pass
#
#     with open(filename, 'a', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#         if not file_exists:
#             writer.writeheader()
#
#         writer.writerow(second_data)
# except Exception as ex:
#     print(f'Ошибка {str(ex)}')

def find_person(filename, name):
    try:
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                if row['name'] == name:
                    return row
        return f'сотрудник с именем {name} не найден'

    except FileNotFoundError:
        return 'file not found'
    except Exception as e:
        return f'ошибка {str(e)}'


filename = 'employees.csv'
name = 'Pasha Pestunov'
result = find_person(filename, name)
print(result)

