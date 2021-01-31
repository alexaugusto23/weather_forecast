from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
from flask import request
import os 
import MySQLdb

app = Flask(__name__)

mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

#routes
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    cur = mysql.cursor()
    cur.execute('''SET time_zone= "America/Sao_Paulo" ''')
    cur.execute('''SELECT * FROM weather ORDER BY weather_id DESC LIMIT 1  ''')
    dataindex = cur.fetchall()
    return render_template("index.html", dataindex = dataindex)


@app.route('/dados', methods=['GET', 'POST'])
def dados():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM weather ORDER BY weather_id  ''')
    data = cur.fetchall()
    return render_template("dados.html", data = data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port)