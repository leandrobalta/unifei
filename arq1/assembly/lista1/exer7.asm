#	Escreva, em MIPS assembly, um programa que leia um inteiro N e mostre a soma dos números de 1
#	até N (inclusive). Não deixe o usuário inserir um valor de N menor ou igual a zero. Nesse caso, continue
#	lendo valores N, até que um valor positivo seja digitado. Imprima, como resposta, apenas o valor da soma.
#	Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.text 
.globl main
main:
	li $v0, 5
	syscall 
	move $s0, $v0
	
	ble $v0, 0, main
	
	li $t0, 1 # t0 = 1
	li $t1, 0 # t1 = 0
	
loop:
	bgt $t0, $s0, end
	
	add $t1, $t1, $t0
	
	addi $t0, $t0, 1
		
	j loop
end:
	move $a0, $t1
	li $v0, 1
	syscall