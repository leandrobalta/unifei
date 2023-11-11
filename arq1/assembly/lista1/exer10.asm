#	Escreva, em MIPS assembly, um programa, dividido em dois subprogramas, para: ler 6 valores inteiros
#	informados pelo usuário e armazenar em um array (subprograma), percorrer o array e retornar o maior
#	valor presente (subprograma), imprimir o maior valor (main). Em sua resposta, imprima apenas o maior
#	valor. Não imprima outras mensagens de texto para indicar entrada/saída de dados.

.data 
	array: .space 24
	
.text
.globl main
main: 
	jal read	
	
	jal get_max_value

	move $a0, $s1
	li $v0, 1
	syscall

	li $v0, 10 # finishing program 
	syscall
	
.text
read:
	la $s0, array

	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	addi $s0, $s0, 4
	
	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	addi $s0, $s0, 4
	
	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	addi $s0, $s0, 4
	
	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	addi $s0, $s0, 4
	
	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	addi $s0, $s0, 4
	
	li $v0, 5
	syscall
	sw $v0, ($s0)
	
	jr $ra

.text
get_max_value:
	li $t0, 1       
  	la $t1, array   

  	lw $t2, ($t1)   
  	addi $t1, $t1, 4       

loop:
    	lw $t3, ($t1)          
    	bgt $t3, $t2, update    

	addi $t0, $t0, 1
	beq $t0, 6, end
	
   	addi $t1, $t1, 4        
    	j loop

update:
    	move $t2, $t3           

    	addi $t1, $t1, 4        
    	j loop

end:
	move $s1, $t2
    	jr $ra                  
