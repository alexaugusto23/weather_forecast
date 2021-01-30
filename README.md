# weather_forecast
Aplicação de Crawling em uma Página Web com Scrapy e Python 3.

* Site utilizado para extração de dados: https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp


#### Criando Ambiente Virtual para depedências.
-- Criando Ambiente: py -m venv weather_forecast_venv.   
-- Ativando Ambiente: .\weather_forecast_venv\scripts\activate.

#### Instalando Depedências.
-- Instalando o scrapy: pip install scrapy.
-- Instalando o flsk: pip install flask
-- pip install Flask-MySQLdb
-- pip install mysql-connector-python
-- pip install requests

####
-- deletar o json antigo e gerar um novo no path: '\weather_forecast\weather_forecast\weather.json'
-- Comando para gerar arquivo json: scrapy crawl weather -o weather.json 


#### Criando Configurações do Gerenciador de depedências.
-- Criando arquivo de configurações: pip freeze > requirements.txt

#### Criando o projeto.
Comando para criar o projeto: scrapy startproject weather_forecast

#### Criando Estruturas de dados.
Mongodb
db.weather.insert(
{
    id: "", 
    cidade: "",
    temperatura: "",
    previsao: "",
    sensacao: "",
    umidade: "",
    pressao: "",
    vento:  "",
    horario: ""
})

MySQL ou outro BD Relacional.

CREATE TABLE IF NOT EXISTS weather (
    weather_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	cidade VARCHAR ( 100 ) UNIQUE NOT NULL,
    temperatura VARCHAR ( 4 ) UNIQUE NOT NULL,
    previsao VARCHAR ( 30) UNIQUE NOT NULL,
    sensacao VARCHAR ( 4 ) UNIQUE NOT NULL,
    umidade VARCHAR ( 4 ) UNIQUE NOT NULL,
    pressao VARCHAR ( 10 ) UNIQUE NOT NULL,
    vento VARCHAR ( 10 ) UNIQUE NOT NULL,
	horario_created_on TIMESTAMP NOT NULL
);

SELECT * FROM weather;









