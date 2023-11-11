#	Escreva, em MIPS assembly, um programa que leia as medidas dos 3 lados de um triângulo e informe o
#	tipo de triângulo: equilátero, isósceles ou escaleno. Em sua resposta, imprima apenas o nome do tipo (sem
#	acentos). Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.data
	iso: .asciiz "isosceles"
	esc: .asciiz "escaleno"
	equi: .asciiz "equilatero"
		
.text
.globl main
main: 
	li $v0, 5
	syscall
	move $s1, $v0
	
	li $v0, 5
	syscall
	move $s2, $v0
	
	li $v0, 5
	syscall
	move $s3, $v0
	
	beq $s1, $s2, first_second_equal
	beq $s1, $s3, is_iso
	beq $s2, $s3, is_iso
	
	j is_esc
	
first_second_equal:
	beq $s1, $s3, is_equi
	j is_iso	

is_iso:
	la $a0, iso
	j end

is_equi:
	la $a0, equi
	j end

is_esc:
	la $a0, esc

end: 
	li $v0, 4
	syscall
