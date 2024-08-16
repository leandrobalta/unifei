create role programadores

grant insert, update, delete, select on all tables in schema northwind to programadores

create role gerente

create user usuario with password 'usuario123'

select * from information_schema.role_table_grants where grantee='programadores'

grant programadores to usuario

grant usage on schema northwind to programadores

select * from northwind.categories

revoke delete on table northwind.categories from programadores;

create role dba;

create user user_dba with password 'user_dba';

grant dba to user_dba



grant all on database postgres to user_dba

grant usage on schema northwind to dba