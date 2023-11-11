#	Escreva, em MIPS assembly, um programa que leia um inteiro N e mostre os N primeiros números
#	ímpares. Imprima os números em uma linha, separados entre si por um único espaço. Não imprima outras
#	mensagens de texto para indicar entrada/saída de dados. Atenção: se o usuário informar um valor N = 4, a
#	resposta deve ser: 1 3 5 7


.text
.globl main
main:
	li $v0, 5
	syscall
	move $s0, $v0 # qntd de nmrs para achar
	
	la $t0, 0 # t0 = controlador do loop
	la $t1, 0 # t1 = qntd de impares encontrados
	
loop: 
	beq $s0, $t1, end
	
	andi $t2, $t0, 1
	
	beqz $t2, par
	j impar
	
par: 
	addi $t0, $t0, 1
	j loop	
impar:
	move $a0, $t0
	li $v0, 1
	syscall
	
	li $v0, 11
	li $a0, 32
	syscall
	
	addi $t1, $t1, 1
	addi $t0, $t0, 1
	j loop 

end:
