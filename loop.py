import time 
import json
import os
import MySQLdb

mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

def insert():
    with open ('.\weather_forecast\weather_forecast\weather.json','r', encoding='utf-8') as arquivo_json:
        dados_json = json.load(arquivo_json)       

        cidade =dados_json[0]['cidade']
        temperatura = dados_json[0]['temperatura'][1:3]
        previsao = dados_json[0]['previsao']
        sensacao = dados_json[0]['sensacao'][11:13]
        umidade = dados_json[0]['umidade'][0:2]
        pressao = dados_json[0]['pressao'][0:4]
        vento = dados_json[0]['vento'][7:8]
        
        cur = mysql.cursor()
        cur.execute('''INSERT INTO weather(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (cidade, temperatura, previsao, sensacao, umidade, pressao, vento))
        mysql.commit()
        mysql.close()
    return 'dados inseridos'




insert()

'''
while True:
    insert()
    
    time.sleep(60)    
'''