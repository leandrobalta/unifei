create table aluga (
	id_cliente int,
	id_funcionario int,
	id_copia int,
	dataInicio date not null,
	dataFimPrev date not null,
	dataFim date,
	foreign key (id_funcionario) references funcionario(codigo),
	foreign key (id_cliente) references cliente(codigo),
	foreign key (id_copia) references copia(id),
	primary key (id_funcionario, id_cliente, id_copia),
	check (dataFim is null or dataFim >= dataInicio),
	check (dataFimPrev >= dataInicio)
)


select * from cliente

select * from aluga

select * from copia

select * from filme

select * from funcionario

select * from copia 

insert into filme(codigo, nome, duracao, diretor)
values 
	(6, 'Julie & Julia', 50, 'Woody Allen')


insert into copia (numero, id_filme, status)
values (10, 6, 'Alugado')

insert into aluga (id_cliente, id_funcionario, id_copia, dataInicio, DataFimPrev, DataFim)
values
	(2, 1, 18, '2011-04-10', '2011-04-13', '2011-04-12')

//A
select c.nome, f.diretor
from cliente c
join aluga a
on c.codigo = a.id_cliente
join copia co
on a.id_copia = co.id
join filme f 
on co.id_filme = f.codigo 



//B
select c.nome as NomeCliente, f.nome as NomeFuncionario, co.numero as numeroCopia, fi.nome as NomeFilme, a.dataInicio as DataAlugado
from cliente c
join aluga a
on a.id_cliente = c.codigo

join funcionario f
on f.codigo = a.id_funcionario

join copia co
on co.id = a.id_copia

join filme fi
on fi.codigo = co.id_filme

where fi.nome = 'Julie & Julia' and a.dataInicio < '2011-04-11'

select * from filme
insert into filme (codigo, nome, duracao, diretor)
values
	(7, 'Carros 2', 100, 'Philip Seymour Hoffman.'),
	(8, 'barbie', 100, 'Philip Seymour Hoffman.'),
	(9, 'batman', 100, 'Philip Seymour Hoffman.'),
	(10, 'flash', 100, 'Philip Seymour Hoffman.')
	
select * from copia
insert into copia (numero, id_filme, status)
values
	(1, 7, 'Alugado'),
	(2, 7, 'Disponivel'),
	(1, 10, 'Disponivel'),
	(2, 10, 'Alugado')


select * from ator

alter table ator 
add unique(ator, id_filme)

alter table ator
add column id serial primary key

SELECT CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'ator'
AND CONSTRAINT_TYPE = 'PRIMARY KEY';

alter table ator
alter column ator set not null

select * from ator

insert into ator (ator, id_filme)
values 
	('Philip Seymour Hoffman.', 7),
	('Philip Seymour Hoffman.', 8),
	('Philip Seymour Hoffman.', 9),
	('Philip Seymour Hoffman.', 10)

//C
select f.codigo as CodigoFilme, c.numero as CopiaNumero, c.status as Status, a.ator
from copia c
join filme f
on c.id_filme = f.codigo
join ator a 
on a.id_filme = f.codigo
where a.ator = 'Philip Seymour Hoffman.'
