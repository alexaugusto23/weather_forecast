from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
import os 
import time
from shell_scrapy import Spider
from flask_apscheduler import APScheduler, scheduler
from dados import Dados

app = Flask(__name__)

#routes
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    dataindex = Dados.consulta_bd_index()
    return render_template("index.html", dataindex = dataindex)

@app.route('/dados', methods=['GET', 'POST'])
def dados():
    data = Dados.consulta_bd_dados()
    return render_template("dados.html", data = data)

@app.route("/scrapy", methods=['GET', 'POST'])
def scrapy():
    Spider.scriptscrapy()
    return render_template("scrapy.html", msg = "Scrapy com sucesso!!!")

@app.cli.command()
def scheduled():
    """Run shell scrapy."""
    Spider.scriptscrapy()
    time.sleep(10)
    print("Done Scrapy....")

def scheduled_Task():
    Spider.scriptscrapy()


scheduled_Task()

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(id = 'ScheduledTask', func = scheduled_Task, trigger = 'cron', minute = 1)
    scheduler.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    