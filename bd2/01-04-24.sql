create database indexacao;

show data_directory;

-- 1b

create table departamento (
	numeroDepto int,
	nomeDepto varchar(30) not null,
	primary key(numeroDepto)
)

9
-- 1c 
insert into departamento values (4, 'Recursos Humanos')
insert into departamento values (3, 'Producao')
insert into departamento values (2, 'Financeiro')
insert into departamento values (1, 'Almoxarifado')

delete from departamento


select ctid, * from departamento
