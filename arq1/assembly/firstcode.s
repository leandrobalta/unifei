# r = [m – (2 – n)] – (o + p + 3)
# $s0 → r
# $s1 → m
# $s2 → n
# $s3 → o
# $s4 → p

# starting with (o + p + 3)
add $t0, $s3, $s4
addi $t1, $t0, 3 # $t1 is the final result

# [m – (2 – n)]
subi $t2, $zero, 2
