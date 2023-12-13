import json
d1 = {
    'pessoa 1': {
        'nome': 'wnedll',
        'idade': '27 anos'
    },
    'pessoa 2': {
        'nome': 'luiz',
        'idade': '30 anos'
    },
    
}

d1_json = json.dumps(d1)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
    print(d1_json)