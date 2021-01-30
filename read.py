import json
def ler_json():
        with open ('.\weather.json','r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json

x = ler_json()
for i in x[0]:
    print(x[0]['cidade'])
    print(x[0]['temperatura'][1:3])
    print(x[0]['previsao'])
    print(x[0]['sensacao'][11:13])
    print(x[0]['umidade'][0:2])
    print(x[0]['pressao'][0:4])
    print(x[0]['vento'][5:6])