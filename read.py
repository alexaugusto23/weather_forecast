import json
import os

def ler_json():
        with open ('.\weather_forecast\weather_forecast\weather.json','r') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json

def deletar():
    path = 'c:/git/weather_forecast/weather_forecast/weather_forecast/'

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(file)
            if "weather.json" == file:
                os.remove(file_path)
            else: print("file não encontrado")

#deletar()

x = ler_json()
print(x[0]['vento'][7:8])

'''

    print(x[0]['cidade'])
    print(x[0]['temperatura'][1:3])
    print(x[0]['previsao'])
    print(x[0]['sensacao'][11:13])
    print(x[0]['umidade'][0:2])
    print(x[0]['pressao'][0:4])
    print(x[0]['vento'][5:6])
'''    