#	Escreva, em MIPS assembly, um programa que leia dois valores A e B e passe-os como parâmetros para
#	um subprograma que computa e devolve a soma dos valores no intervalo [A, B]. Em sua resposta, imprima
#	apenas o valor da soma. Não imprima outras mensagens de texto para indicar entrada/saída de dados

.text
.globl main
main:
	li $v0, 5
	syscall
	move $s0, $v0 # s0 = a
	
	li $v0, 5
	syscall
	move $s1, $v0 # s1 = b
	
	jal sum
	
	move $a0, $s3
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
.text
sum:
	add $s3, $s0, $s1
	jr $ra