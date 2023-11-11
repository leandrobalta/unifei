#	Escreva, em MIPS assembly, um programa que leia 4 valores inteiros e os armazene em um array A. A
#	seguir, leia 6 inteiros e os armazene em um array B. Crie um subprograma que compute e retorne quantos
#	elementos estão presentes em A e B simultaneamente. O main deve imprimir a resposta. Não imprima
#	outras mensagens de texto para indicar entrada/saída de dados
.data
A: .space 16     
B: .space 24     

.text
.globl main

main:
    jal read_A      
    jal read_B      
    jal count_common_elements  

    move $a0, $v0    
    li $v0, 1         
    syscall         

    li $v0, 10      
    syscall         

read_A:
    la $t0, A       

    li $t1, 4       
    li $t2, 0       

loop_A:
    li $v0, 5       
    syscall         
    sw $v0, ($t0)   

    addi $t0, $t0, 4  
    addi $t2, $t2, 1  

    bne $t2, $t1, loop_A 

    jr $ra          

read_B:
    la $t0, B       

    li $t1, 6       
    li $t2, 0       

loop_B:
    li $v0, 5       
    syscall         
    sw $v0, ($t0)  

    addi $t0, $t0, 4  
    addi $t2, $t2, 1  

    bne $t2, $t1, loop_B  

    jr $ra          

count_common_elements:
    la $t0, A       
    la $t1, B       

    li $t2, 0       
    li $t3, 4       
    li $t4, 6       

outer_loop:
    lw $t5, ($t0)   

    la $t6, B       
    li $t7, 6       

inner_loop:
    lw $t8, ($t6)   

    beq $t5, $t8, increment_counter  

    addi $t6, $t6, 4   
    addi $t7, $t7, -1 

    bnez $t7, inner_loop 

    addi $t0, $t0, 4  
    addi $t3, $t3, -1 

    bnez $t3, outer_loop 

    move $v0, $t2   

    jr $ra          

increment_counter:
    addi $t2, $t2, 1

    jr $ra          