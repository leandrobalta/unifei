#Escreva, em MIPS assembly, um programa que leia um valor inteiro e o repasse para um subprograma.
#Se o valor for um quadrado perfeito, o subprograma deve retornar 1; caso contrário, retornar zero. O main
#deve imprimir como resposta apenas o valor retornado. Em sua resposta, imprima apenas o maior valor.
#Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.text
.globl main
main: 
    	li $v0, 5
    	syscall
    	move $t1, $v0

  	jal is_perfect_square
  	
  	li $v0, 1
  	syscall
  	
  	li $v0, 10
  	syscall  


.text
is_perfect_square: 
    li $v1, 1

    loop: 
        # v1 * v1 => t0
        mul $t0, $v1, $v1
        beq $t0, $t1, isSquare # se t0 == t1, entao eh quadrado perfeito
        bgt $t0, $t1, isNotSquare # se t0 > t1, entao nao eh quadrado perfeito

        # v1 = v1 + 1
        addi $v1, $v1, 1
        j loop # volta para o loop

    isSquare: 
        li $a0, 1
        jr $ra

    isNotSquare: 
        li $a0, 0
        jr $ra