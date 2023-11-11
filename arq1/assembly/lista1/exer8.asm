#	Escreva, em MIPS assembly, um programa que leia um inteiro N e mostre o seu fatorial. Imprima
#	apenas o valor do fatorial como resposta. Não imprima outras mensagens de texto para indicar
#	entrada/saída de dados.

.text 
.globl main
main:
	li $v0, 5
	syscall 
	move $s0, $v0
	
	ble $v0, 0, main
	
	li $t0, 1 # t0 = 1
	li $t1, 1 # t1 = 0
	
loop:
	bgt $t0, $s0, end
	
	mul $t1, $t1, $t0
	
	addi $t0, $t0, 1
		
	j loop
end:
	move $a0, $t1
	li $v0, 1
	syscall