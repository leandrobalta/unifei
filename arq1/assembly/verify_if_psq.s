

.text
.globl main
main: 

    # t1 = input do usuario
    li $t1, 5
    syscall

    # v0 = 1, inicio v0 com o valor 1 
    li $v1, 1

    loop: 
        # v1 * v1 => v0
        mul $v0, $v1, $v1
        beq $v0, $t1, isSquare # se v0 == t1, entao eh quadrado perfeito
        bgt $v0, $t1, isNotSquare # se v0 > t1, entao nao eh quadrado perfeito

        # v1 = v1 + 1
        addi $v1, $v1, 1
        j loop # volta para o loop

    isSquare: 
        li 1, 10
        syscall

    isNotSquare: 
        li 0, 10
        syscall