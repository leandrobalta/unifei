#Escreva, em MIPS assembly, um programa que leia 4 valores inteiros digitados pelo usuário e mostre
#qual o maior deles. Em sua resposta, imprima apenas o maior dos 4 valores digitados. Não imprima outras
#mensagens de texto para indicar entrada/saída de dados.

.text
.globl main
main: 
	li $v0, 5
	syscall
	move $s0, $v0
	
	li $v0, 5
	syscall
	move $s1, $v0
	
	li $v0, 5
	syscall
	move $s2, $v0
	
	li $v0, 5
	syscall
	move $s3, $v0
	
	sgt $t1, $s0, $s1 # if (s0 > s1 )
	
	sgt $t2, $s2, $s3 # if (s2 > s3 )
	
	beqz $t1, second_bigger_than_first 
	j first_bigger_than_second
	
first_bigger_than_second:
	addi $t3, $s0, 0
	j continue_check	

second_bigger_than_first:
	addi $t3, $s1, 0
	
continue_check:
	beqz $t2, fourth_bigger_than_third
	j third_bigger_than_fourth
	
third_bigger_than_fourth:	
	addi $t4, $s2, 0
	j final_check	

fourth_bigger_than_third:
	addi $t4, $s3, 0
	
final_check:
	sgt $t5, $t3, $t4 # if ( $t3 > $t4 ) 
	beqz $t5, t4_bigger
	j t3_bigger

t3_bigger: 
	la $a0, ($t3)
	j end
	
t4_bigger:
	la $a0, ($t4)

end:
	li $v0, 1
	syscall