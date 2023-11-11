#	Escreva, em MIPS assembly, um programa que leia a idade e o tempo de serviço de um trabalhador e
#	informe se ele pode ou não se aposentar. As condições para aposentadoria são:
#	• Ter pelo menos 65 anos OU
#	• Ter trabalhado pelo menos 35 anos OU
#	• Ter pelo menos 60 anos e ter trabalhado pelo menos 30 anos.
#	Em sua resposta, imprima apenas as palavras “sim” ou “nao” (sem acento). Não imprima outras
#	mensagens de texto para indicar entrada/saída de dados.

.data
	yes: .asciiz "sim"
	no:  .asciiz "nao"

.text
.globl main

main: 
	li $v0, 5
	syscall
	move $s0, $v0 # $s0 = idade do rapaz
	
	li $v0, 5
	syscall
	move $s1, $v0 # s1 = tempo de servico do home
	
	bge $s0, 65, can_retire 
	bge $s1, 35, can_retire
	bge $s0, 60, check_worked_years 
	
	j cant_retire
	
check_worked_years:
	bge $s1, 30, can_retire
	j cant_retire

can_retire:
	la $a0, yes
	j end
	
cant_retire:
	la $a0, no

end: 
	li $v0, 4
	syscall