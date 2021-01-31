import json

def ler_json():
        with open ('.\weather_forecast\weather_forecast\weather.json','r') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json

x = ler_json()
print(x[0]['vento'][6:9])

'''

    print(x[0]['cidade'])
    print(x[0]['temperatura'][1:3])
    print(x[0]['previsao'])
    print(x[0]['sensacao'][11:13])
    print(x[0]['umidade'][0:2])
    print(x[0]['pressao'][0:4])
    print(x[0]['vento'][5:6])
'''    