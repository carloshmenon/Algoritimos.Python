

create database suicidio;

use suicidio;

-- 1. Tabelas de Referência
CREATE TABLE Estados (
    id_estado INT PRIMARY KEY,
    sigla_estado VARCHAR(2)
);

CREATE TABLE Estado_civil (
    id_estado_civil INT PRIMARY KEY,
    estciv VARCHAR(50)
);

CREATE TABLE Escolaridade (
    id_escolaridade INT PRIMARY KEY,
    esc VARCHAR(100)
);

CREATE TABLE Causas (
    id_causa INT PRIMARY KEY,
    causabas VARCHAR(10),
    causabas_o VARCHAR(255)
);

-- 2. Tabela Principal (Sem restrições de integridade)
CREATE TABLE Suicidios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ano INT,
    idade INT,
    sexo CHAR(1),
    estado_id INT,
    estado_civil_id INT,
    escolaridade_id INT,
    causa_id INT
);

INSERT INTO Estados (id_estado, sigla_estado) VALUES
(1, 'AC'),
(2, 'AL'),
(3, 'AP'),
(4, 'AM'),
(5, 'BA'),
(6, 'CE'),
(7, 'DF'),
(8, 'ES'),
(9, 'GO'),
(10, 'MA'),
(11, 'MT'),
(12, 'MS'),
(13, 'MG'),
(14, 'PA'),
(15, 'PB'),
(16, 'PR'),
(17, 'PE'),
(18, 'PI'),
(19, 'RJ'),
(20, 'RN'),
(21, 'RS'),
(22, 'RO'),
(23, 'RR'),
(24, 'SC'),
(25, 'SP'),
(26, 'SE'),
(27, 'TO');



INSERT INTO Estado_civil (id_estado_civil, estciv) VALUES
(1, 'Solteiro/a'),
(2, 'Casado/a'),
(3, 'NA'),
(4, 'Viúvo/a');

INSERT INTO Escolaridade (id_escolaridade, esc) VALUES
(1, '1 a 3 anos'),
(2, '4 a 7 anos'),
(3, '8 a 11 anos'),
(4, 'NA');

INSERT INTO Causas (id_causa, causabas, causabas_o) VALUES
(1, 'X609', NULL),
(2, 'X629', NULL),
(3, 'X689', NULL),
(4, 'X699', NULL),
(5, 'X700', NULL),
(6, 'X702', NULL),
(7, 'X709', NULL),
(8, 'X720', NULL),
(9, 'X740', NULL),
(10, 'X747', NULL),
(11, 'X749', NULL),
(12, 'X780', NULL);

ALTER TABLE Suicidios
MODIFY COLUMN idade DATE;

INSERT INTO Suicidios
(ano, idade, sexo, estado_id, estado_civil_id, escolaridade_id, causa_id)
VALUES
(2010,'1999-11-09','M',1,1,1,12),
(2010,'1985-09-23','M',1,1,1,12),
(2010,'1995-08-06','M',1,1,1,12),
(2010,'1983-12-25','F',1,2,1,12),
(2010,'1982-05-13','M',1,2,4,8),
(2010,'1967-07-13','F',1,1,2,12),
(2010,'1979-09-05','M',1,1,2,5),
(2010,'1994-01-19','M',1,1,4,5),
(2010,'1952-04-14','M',1,1,4,2),
(2010,'1968-08-14','M',1,1,4,10),
(2010,'1971-11-23','M',1,1,4,5),
(2010,'1954-02-15','M',1,3,4,5),
(2010,'1971-12-25','F',1,2,4,4),
(2010,NULL,'M',1,1,4,7),
(2010,'1984-10-06','M',1,1,4,9),
(2010,'1995-09-14','M',1,1,4,11),
(2010,'1948-12-21','M',1,1,4,2),
(2010,'1995-12-31','F',1,1,4,3),
(2010,'1981-07-06','M',1,3,4,7),
(2010,'1987-08-06','M',1,1,3,5),
(2010,'1972-09-16','M',1,3,4,5),
(2010,'1975-01-12','F',1,3,4,1),
(2010,'1982-01-23','M',1,1,2,6),
(2010,'1966-11-05','M',1,2,4,7),
(2010,'1987-12-08','M',1,1,4,5),
(2010,'1971-12-30','M',1,3,4,7),
(2010,'1978-07-27','M',1,3,4,5);

INSERT INTO Escolaridade (id_escolaridade, esc) VALUES
(5, 'Nenhuma'),
(6, '12 e mais');

INSERT INTO Causas (id_causa, causabas, causabas_o) VALUES
(13, 'X649', NULL),
(14, 'X718', NULL),
(15, 'X750', NULL),
(16, 'X800', NULL);

INSERT INTO Suicidios
(ano, idade, sexo, estado_id, estado_civil_id, escolaridade_id, causa_id)
VALUES
(2010,'1971-05-28','M',1,3,4,5),
(2010,'1995-08-23','F',1,1,4,3),
(2010,'1979-01-31','M',1,3,4,2),
(2010,'1925-10-10','M',1,1,4,5),
(2010,'1949-03-15','M',1,3,4,5),
(2010,'1979-10-18','M',1,2,5,5),
(2010,'1965-02-16','M',1,1,5,5),
(2010,'1988-05-20','M',1,1,6,16),
(2010,'1987-11-25','M',1,1,2,2),
(2010,'1971-05-15','F',1,3,4,7),
(2010,'1984-12-26','F',1,3,4,7),
(2010,'1983-09-24','F',1,4,3,7),
(2010,'1991-02-03','M',1,3,4,7),
(2010,'1983-10-22','M',1,3,4,7),
(2010,'1965-10-01','M',2,2,2,7),
(2010,NULL,'M',2,3,4,7),
(2010,'1985-05-05','M',2,1,2,7),
(2010,'1972-12-25','F',2,3,4,7),
(2010,'1979-07-31','M',2,1,4,14),
(2010,'1993-03-12','F',2,1,4,5),
(2010,'1986-05-31','M',2,1,4,15),
(2010,'1957-04-16','F',2,1,4,13),
(2010,'1936-12-16','M',2,2,4,13);

SELECT COUNT(*) AS total_registros
FROM Suicidios;

-- 1 view
CREATE VIEW vw_idade_sexo_estado AS
SELECT
    s.idade,
    s.sexo,
    e.sigla_estado AS estado
FROM Suicidios s
JOIN Estados e
    ON s.estado_id = e.id_estado;
    
SELECT * FROM vw_idade_sexo_estado;

-- 2 view
CREATE VIEW vw_total_suicidios_por_estado AS
SELECT
    e.sigla_estado AS estado,
    COUNT(*) AS total_suicidios
FROM Suicidios s
JOIN Estados e
    ON s.estado_id = e.id_estado
GROUP BY e.sigla_estado;

SELECT * FROM vw_total_suicidios_por_estado;

-- 3 view
CREATE VIEW vw_top10_estados_suicidios AS
SELECT
    e.sigla_estado AS estado,
    COUNT(*) AS total_casos
FROM Suicidios s
JOIN Estados e
    ON s.estado_id = e.id_estado
GROUP BY e.sigla_estado
ORDER BY total_casos DESC
LIMIT 10;

SELECT * FROM vw_top10_estados_suicidios;

-- 4 view
CREATE VIEW vw_casos_por_escolaridade AS
SELECT
    e.esc AS escolaridade,
    COUNT(*) AS total_casos
FROM Suicidios s
JOIN Escolaridade e
    ON s.escolaridade_id = e.id_escolaridade
GROUP BY e.esc;

SELECT * FROM vw_casos_por_escolaridade;

-- 5 view
CREATE VIEW vw_casos_por_estado_civil AS
SELECT
    ec.estciv AS estado_civil,
    COUNT(*) AS total_casos
FROM Suicidios s
JOIN Estado_civil ec
    ON s.estado_civil_id = ec.id_estado_civil
GROUP BY ec.estciv;

SELECT * FROM vw_casos_por_estado_civil;

-- 6 view
CREATE VIEW vw_data_nascimento_por_estado AS
SELECT
    e.sigla_estado AS estado,
    s.idade AS data_nascimento
FROM Suicidios s
JOIN Estados e
    ON s.estado_id = e.id_estado;
    
SELECT * FROM vw_data_nascimento_por_estado;

-- 7 view
CREATE VIEW vw_relatorio_casos AS
SELECT
    e.sigla_estado AS estado,
    ec.estciv AS estado_civil,
    es.esc AS escolaridade,
    c.causabas AS causa,
    COUNT(*) AS quantidade_casos
FROM Suicidios s
JOIN Estados e
    ON s.estado_id = e.id_estado
JOIN Estado_civil ec
    ON s.estado_civil_id = ec.id_estado_civil
JOIN Escolaridade es
    ON s.escolaridade_id = es.id_escolaridade
JOIN Causas c
    ON s.causa_id = c.id_causa
GROUP BY
    e.sigla_estado,
    ec.estciv,
    es.esc,
    c.causabas;
    
SELECT * FROM vw_relatorio_casos;


SELECT * FROM Suicidios;
SELECT * FROM Estados;
SELECT * FROM Estado_civil;
SELECT * FROM Escolaridade;
SELECT * FROM Causas;


