create table Resultados(
	id_resultado SERIAL PRIMARY KEY,
	ano INTEGER,
	colocacao INTEGER,
	categoria VARCHAR(20),
	numero_peito INTEGER,
	nome VARCHAR(70),
	equipe VARCHAR(50),
	pace VARCHAR(10),
	tempo VARCHAR(10),
	genero CHAR(1)	
);
--ano,colocacao,categoria,numero_peito,nome,equipe,pace,tempo,genero
SELECT COUNT(*) 
FROM Resultados;
SELECT * FROM resultados;