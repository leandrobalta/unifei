#Escreva, em MIPS assembly, um programa que leia um único valor inteiro digitado pelo usuário e
#informe se o valor digitado é positivo ou negativo. Em sua resposta, imprima apenas as palavras “positivo”
#ou “negativo”. Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.data
	pos: .asciiz "positivo"
	negative: .asciiz "negativo"
	zero: .word 0
.text
.globl main
main:
	li $t0, 0
	li $v0, 5
	syscall
	bge $v0, $t0, is_positive
	j is_negative
	
is_positive:
	la $a0, pos
	j end

is_negative:
	la $a0, negative
	j end
	
end:
	li $v0, 4
	syscall
	