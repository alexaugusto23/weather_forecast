import json

def ler_json():
        with open ('.\weather_forecast\weather_forecast\weather.json','r') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json

generic = ler_json()
vento = generic[0]['vento'].split()
valor = vento[2][0] + vento[2][1]
elementos = list(valor)
print(elementos)
low = elementos[1].lower()
print(low)
if 'k' in elementos[1].lower():
    valor_test = elementos.pop(0)
    print(valor_test)
    vento_test = valor_test 
    print(True)
else:
    valor_test = elementos[0] + elementos[1]
    vento_test = valor_test 
    print(False)
print(vento_test)



'''

    print(x[0]['cidade'])
    print(x[0]['temperatura'][1:3])
    print(x[0]['previsao'])
    print(x[0]['sensacao'][11:13])
    print(x[0]['umidade'][0:2])
    print(x[0]['pressao'][0:4])
    print(x[0]['vento'][5:6])
'''    