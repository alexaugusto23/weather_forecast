import os
from flask_mysqldb import MySQL
from flask import Flask, render_template , redirect, url_for,request

app = Flask(__name__)

app.config['MYSQL_USER'] = 'adminMaster'
app.config['MYSQL_PASSWORD'] =
app.config['MYSQL_HOST'] = 'database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'dbmysql'

mysql = MySQL(app)

#routes
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    id_scrapy = 1,
    cidade = "São-Paulo"
    temperatura = "28"
    previsao = "Alguma Nebulosidade"
    sensacao = "30"
    umidade = "82"
    pressao = "924"
    vento = "19"
    horario = "11:47"

    return render_template("index.html", 
                            cidade=cidade, 
                            temperatura=temperatura, 
                            previsao=previsao,
                            sensacao=sensacao,
                            umidade=umidade,
                            pressao=pressao,
                            vento=vento,
                            horario=horario)

def admin():
    admin = Log.query.all()
    return render_template("admin.html", admin=admin)


@app.route('/users', methods=['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM weather''')
    rv = cur.fetchall()
    cur.close()
    return str(rv)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port)