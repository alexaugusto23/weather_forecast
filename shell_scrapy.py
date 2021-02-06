import os
from connection import mysql
import os
import json

class Spider:

    def scriptscrapy():
        
        #Deletando e criando json
        #os.chdir("C:/git/weather_forecast") #local
        os.chdir("/home/site/wwwroot") #azure
        path = os.getcwd()
        path1 = os.path.join(path,"weather_forecast")
        path2 = os.path.join(path1,"weather_forecast")
        
        print(f'path2: {path2}')
        chdir = os.chdir(path2)
        path_file = os.path.join(path2,"weather.json")
        print(path_file)
        for root, dirs, files in os.walk(".", topdown=False):
            for file_name in files:
                #print(os.path.join(root, file_name))
                if "weather.json" == file_name:
                    print(True)
                    os.remove(path_file)
                    print("-"*80)
                    print("Arquivo weather.json removido.......")
                else:
                    print("Criando weather.json")
        os.system("scrapy crawl weather -o weather.json")
        os.system("cls")
        print("-"*80)
        print("Criação do weather.json concluído.......")


        #Inserindo no banco de dados
        get_path_atual = os.getcwd()+"/weather.json"

        with open (get_path_atual,'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)       

            cidade =dados_json[0]['cidade']
            temperatura = dados_json[0]['temperatura'][1:3]
            previsao = dados_json[0]['previsao']
            sensacao = dados_json[0]['sensacao'][11:13]
            umidade = dados_json[0]['umidade'][0:2]
            pressao = dados_json[0]['pressao'][0:4]
            vento = dados_json[0]['vento'].split()

            valor = vento[2][0] + vento[2][1]
            elementos = list(valor)
            if ('k' in elementos[1].lower()):
                valor = elementos.pop(0)
                vento = valor
            else:
                valor = elementos[0] + elementos[1]
                vento = valor
            
            cur = mysql.cursor()
            cur.execute('''INSERT INTO weather(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (cidade, temperatura, previsao, sensacao, umidade, pressao, vento))
            mysql.commit()
            mysql.cursor().close()
            arquivo_json.close()
            print("-"*80)
            print("Insert no DB concluído.......")