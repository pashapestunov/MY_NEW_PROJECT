

import json

# Чтение данных из файла JSON
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


