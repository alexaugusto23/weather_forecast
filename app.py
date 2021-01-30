import os
import MySQLdb
from flask import Flask, render_template , redirect, url_for,request
import datetime
import json

#d = dir(MySQLdb)
#print(d)
app = Flask(__name__)

mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

#routes
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM weather ORDER BY weather_id DESC LIMIT 1  ''')
    dataindex = cur.fetchall()
    return render_template("index.html", dataindex = dataindex)


@app.route('/dados', methods=['GET', 'POST'])
def dados():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM weather ORDER BY weather_id  ''')
    data = cur.fetchall()
    return render_template("dados.html", data = data)


@app.route('/insert', methods=['GET', 'POST'])
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
    return 'dados inseridos'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port)

