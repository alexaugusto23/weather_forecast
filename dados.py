from connection import mysql

class Dados:

    def consulta_bd_index():
        cur = mysql.cursor()
        cur.execute(''' SET time_zone= "America/Sao_Paulo" ''')
        cur.execute(''' SELECT * FROM weather ORDER BY weather_id DESC LIMIT 1  ''')
        dataindex = cur.fetchall()
        mysql.cursor().close()
        return dataindex
    
    def consulta_bd_dados():
        cur = mysql.cursor()
        cur.execute('''SELECT * FROM weather ORDER BY weather_id  ''')
        data = cur.fetchall()
        mysql.cursor().close()
        return data