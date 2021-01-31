import json
import MySQLdb
import os
import time

mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

def insert():
    path = os.getcwd()
    os.chdir(path+'/weather_forecast/weather_forecast/')
    path = os.getcwd()
    conc = path+'/weather.json'

    with open (conc,'r', encoding='utf-8') as arquivo_json:
        dados_json = json.load(arquivo_json)       

        cidade =dados_json[0]['cidade']
        temperatura = dados_json[0]['temperatura'][1:3]
        previsao = dados_json[0]['previsao']
        sensacao = dados_json[0]['sensacao'][11:13]
        umidade = dados_json[0]['umidade'][0:2]
        pressao = dados_json[0]['pressao'][0:4]
        generic = dados_json[0]['vento'].split()
        xgeneric = generic[2][0:2]
        vento = xgeneric
        
        cur = mysql.cursor()
        cur.execute('''INSERT INTO weather(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (cidade, temperatura, previsao, sensacao, umidade, pressao, vento))
        mysql.commit()
        mysql.close()
        arquivo_json.close()
    return print('dados inseridos')

#insert()