-- 3a

select * from pg_indexes where tablename='departamento'

-- 3a a departamento_pkey
-- 3a b primario e denso
-- 3a c btree

--QUESTÃO 4A
CREATE TYPE sexo_t AS ENUM ('M', 'F');

CREATE TABLE funcionario(
	numeroRegistro SERIAL UNIQUE NOT NULL,
	nomeFunc varchar(30) not null,
	sexo sexo_t not null,
	dataNasc date not null,
	depto int not null,	
	primary key(numeroRegistro)
)

insert into funcionario (
 nomeFunc, sexo, dataNasc, depto
)
select
 substr(md5(random()::varchar(30)), 0, 30),
(enum_range(NULL::sexo_t))[floor(random() * (2-1 + 1) + 1)],
 date(timestamp '1990-01-01' + random() * (timestamp '1990-12-31' - timestamp
'2000-01-01')), floor(random()* (4-1 + 1) + 1)
from generate_series(1, 1000000) s(i)

select ctid, * from funcionario order by ctid desc

CREATE INDEX funcionario_depto_index ON funcionario USING btree(depto)

select * from pg_indexes where tablename = 'funcionario'