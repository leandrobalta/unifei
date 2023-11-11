#	Escreva, em MIPS assembly, um programa que leia um inteiro N e implemente um contador regressivo,
#	mostrando na tela os números de N até 1. Imprima os números em uma linha, separados entre si por um
#	único espaço. Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.text 
.globl main
main:
	li $v0, 5
	syscall
	move $s0, $v0
	
	addi $s0, $s0, 1  
loop: 
	beq $s0, 1, end
	
	subi $s0, $s0, 1
	
	move $a0, $s0
	li $v0, 1
	syscall
	
	li $v0, 11
	li $a0, 32
	syscall
	
	j loop
end: 
