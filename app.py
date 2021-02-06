from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
import os 
import MySQLdb
import time
import shell_scrapy
from flask_apscheduler import APScheduler, scheduler

app = Flask(__name__)
scheduler = APScheduler()
mysql = MySQLdb.Connection(user='adminMaster', passwd='Mag#2923', host='database-sql.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com', db='dbmysql')

#routes
@app.route("/")
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

@app.route("/scrapy", methods=['GET', 'POST'])
def scrapy():
    shell_scrapy.scriptscrapy()
    return render_template("scrapy.html", msg = "Scrapy com sucesso!!!")


@app.cli.command()
def scheduled():
    """Run shell scrapy."""
    shell_scrapy.scriptscrapy()
    time.sleep(10)
    print("Done Scrapy....")

def scheduled_Task():
    shell_scrapy.scriptscrapy()

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func = scheduled_Task, trigger = 'interval', seconds = 60)

    scheduler.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port)