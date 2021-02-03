from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
import json
import os 
import MySQLdb
import time



app = Flask(__name__)

mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

#routes
@app.route("/")
def loop():
        while True:
            #Deletando e criando json
            chdir = os.chdir("C:/git/weather_forecast")
            path = os.getcwd()
            path1 = os.path.join(path,"weather_forecast")
            path2 = os.path.join(path1,"weather_forecast")
            print(f'path1: {path}')
            print(f'path1: {path1}')
            print(f'path2: {path2}')
            chdir = os.chdir(path2)
            print(f'Chdir: {chdir}')
            path_file = os.path.join(path2,"weather.json")
            print(path_file)
            for root, dirs, files in os.walk(".", topdown=False):
                for file_name in files:
                    #print(os.path.join(root, file_name))
                    if "weather.json" == file_name:
                        print(True)
                        os.remove(path_file)
                        print("Arquivo Removido")
                    else:
                        print("Criando weather.json")
            os.system("scrapy crawl weather -o weather.json")
            
            os.system("cls")

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
        
            time.sleep(10)


@app.route("/index", methods=['GET', 'POST'])
def index():
    cur = mysql.cursor()
    cur.execute(''' SET time_zone= "America/Sao_Paulo" ''')
    cur.execute(''' SELECT * FROM weather ORDER BY weather_id DESC LIMIT 1  ''')
    dataindex = cur.fetchall()
    mysql.cursor().close()

    return render_template("index.html", dataindex = dataindex)


@app.route('/dados', methods=['GET', 'POST'])
def dados():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM weather ORDER BY weather_id  ''')
    data = cur.fetchall()
    mysql.cursor().close()
    return render_template("dados.html", data = data)


@app.route('/scrapy', methods=['GET', 'POST'])
def scrapy():
    
    #Deletando e criando json
    chdir = os.chdir("C:/git/weather_forecast")
    path = "C:/git/weather_forecast/weather_forecast"
    path = os.getcwd()
    path1 = os.path.join(path,"weather_forecast")
    path2 = os.path.join(path1,"weather_forecast")
    print(f'path1: {path}')
    print(f'path1: {path1}')
    print(f'path2: {path2}')
    os.chdir(path2)
    path_file = os.path.join(path2,"weather.json")
    print(path_file)
    for root, dirs, files in os.walk(".", topdown=False):
        for file_name in files:
            #print(os.path.join(root, file_name))
            if "weather.json" == file_name:
                print(True)
                os.remove(path_file)
                print("Arquivo Removido")
            else:
                print("Criando weather.json")
    os.system("scrapy crawl weather -o weather.json")
    os.system("cls")


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

    return render_template("scrapy.html", msg = 'Scrapy Concluído!')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port)