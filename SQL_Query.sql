USE dbmysql;
SHOW DATABASES;

SET time_zone='America/Sao_Paulo';

CREATE TABLE IF NOT EXISTS weather (
    weather_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	cidade VARCHAR ( 100 ) NOT NULL,
    temperatura VARCHAR ( 4 ) NOT NULL,
    previsao VARCHAR ( 30) NOT NULL,
    sensacao VARCHAR ( 4 ) NOT NULL,
    umidade VARCHAR ( 4 ) NOT NULL,
    pressao VARCHAR ( 10 ) NOT NULL,
    vento VARCHAR ( 10 ) NOT NULL,
	horario_created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE weather;

SELECT * FROM weather;

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','25', 'Alguma nebolusidade', '24', '61', '1010', '15'),
    ('São Paulo','26', 'Alguma nebolusidade', '25', '60', '1011', '16');

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','28', 'Alguma nebolusidade', '29', '55', '1010', '15');

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','30', 'Alguma nebolusidade', '29', '55', '1010', '15');

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','29', 'Poucas Nuvens', '29', '45', '1012', '19');

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','18', 'Chuva', '17', '90', '1050', '30');
    
INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','40', 'Ensolarado', '42', '30', '900', '20');

INSERT INTO weather 
(cidade, temperatura, previsao, sensacao, umidade, pressao, vento) 
VALUES
    ('São Paulo','50', 'Super - Ensolarado', '52', '20', '800', '25');

TRUNCATE TABLE weather;
    
SELECT * FROM weather;