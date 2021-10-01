"""
Melhorando requisições https
Modelo : 01
Standart

Primeiro tempo : Tempo de duração foi de 0.00133 segundos
Segundo tempo  :  Tempo de duração foi de 0.00108 segundo

"""

import requests
import json
import datetime

url = "https://exchange.vcoud.com/coronavirus/latest"
resp = json.loads(requests.get(url).text)

inicio = datetime.datetime.now()
for elem in resp:
    print("%s    %s "%(elem['name'],elem['totalCases']))

tempo_atual = datetime.datetime.now() - inicio
print(f'Tempo de duração foi de {tempo_atual.total_seconds():.5f} segundos')