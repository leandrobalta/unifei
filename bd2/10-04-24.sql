--  INDEXACAO PARTE 2

--2
select * from pg_indexes where tablename='log_logradouro'

--3a
explain analyse select * from cep.log_logradouro
--"Seq Scan on log_logradouro  (cost=0.00..24012.85 rows=909585 width=146) (actual time=0.029..74.170 rows=909585 loops=1)"
--"Planning Time: 0.037 ms"
--"Execution Time: 97.862 ms"

--3b
explain analyse select * from pg_indexes where tablename='log_logradouro'
--"cep"	"log_logradouro"	"log_logradouro_pkey"		"CREATE UNIQUE INDEX log_logradouro_pkey ON cep.log_logradouro USING btree (log_nu_sequencial)"

--3c
explain analyse select * from cep.log_logradouro where log_nu_sequencial < 10

--3d
explain analyse select * from cep.log_logradouro where log_nu_sequencial > 10

--3e
explain analyse select * from cep.log_logradouro where log_nu_sequencial = 15

--3f
explain analyse delete from cep.log_logradouro where log_nu_sequencial = 15

--3g
explain analyse select * from cep.log_logradouro where log_nu_sequencial = 15;


-- 4)
--a) Recuperar todos os registros da tabela log_logradouro onde ufe_sg = 'AC' e log_tipo_logradouro = 'Avenida';
explain analyse select * from cep.log_logradouro where ufe_sg = 'AC' and log_tipo_logradouro = 'Avenida';

--RESULTS:
-- "Gather  (cost=1000.00..21622.51 rows=206 width=146) (actual time=0.396..57.248 rows=139 loops=1)"
-- "  Workers Planned: 2"
-- "  Workers Launched: 2"
-- "  ->  Parallel Seq Scan on log_logradouro  (cost=0.00..20601.91 rows=86 width=146) (actual time=31.419..53.074 rows=46 loops=3)"
-- "        Filter: (((ufe_sg)::text = 'AC'::text) AND ((log_tipo_logradouro)::text = 'Avenida'::text))"
-- "        Rows Removed by Filter: 303148"
-- "Planning Time: 0.046 ms"
-- "Execution Time: 57.268 ms"


--b) Crie um índice (btree) na coluna ufe_sg da tabela log_logradouro
create index ufe_sg_idx on cep.log_logradouro using btree(ufe_sg)

--c) Refaça a questão a.
explain analyse select * from cep.log_logradouro where ufe_sg = 'AC' and log_tipo_logradouro = 'Avenida';

--RESULTS:
-- "Bitmap Heap Scan on log_logradouro  (cost=37.95..8149.49 rows=206 width=146) (actual time=0.107..0.841 rows=139 loops=1)"
-- "  Recheck Cond: ((ufe_sg)::text = 'AC'::text)"
-- "  Filter: ((log_tipo_logradouro)::text = 'Avenida'::text)"
-- "  Rows Removed by Filter: 3126"
-- "  Heap Blocks: exact=74"
-- "  ->  Bitmap Index Scan on ufe_sg_idx  (cost=0.00..37.89 rows=3396 width=0) (actual time=0.090..0.090 rows=3265 loops=1)"
-- "        Index Cond: ((ufe_sg)::text = 'AC'::text)"
-- "Planning Time: 0.129 ms"
-- "Execution Time: 0.863 ms"


--d) Crie um índice (btree) na coluna log_tipo_logradouro da tabela log_logradouro
create index log_tipo_logradouro_idx on cep.log_logradouro using btree(log_tipo_logradouro)

--e) Refaça a questão a.
explain analyse select * from cep.log_logradouro where ufe_sg = 'AC' and log_tipo_logradouro = 'Avenida';

-- RESULTS:
-- "Bitmap Heap Scan on log_logradouro  (cost=644.53..1395.52 rows=206 width=146) (actual time=2.474..2.507 rows=139 loops=1)"
-- "  Recheck Cond: (((ufe_sg)::text = 'AC'::text) AND ((log_tipo_logradouro)::text = 'Avenida'::text))"
-- "  Heap Blocks: exact=29"
-- "  ->  BitmapAnd  (cost=644.53..644.53 rows=206 width=0) (actual time=2.467..2.468 rows=0 loops=1)"
-- "        ->  Bitmap Index Scan on ufe_sg_idx  (cost=0.00..37.89 rows=3396 width=0) (actual time=0.074..0.074 rows=3265 loops=1)"
-- "              Index Cond: ((ufe_sg)::text = 'AC'::text)"
-- "        ->  Bitmap Index Scan on log_tipo_logradouro_idx  (cost=0.00..606.28 rows=55181 width=0) (actual time=2.386..2.386 rows=56624 loops=1)"
-- "              Index Cond: ((log_tipo_logradouro)::text = 'Avenida'::text)"
-- "Planning Time: 0.120 ms"
-- "Execution Time: 2.525 ms"


-- 5)

