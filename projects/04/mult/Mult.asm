// operation: R2 = R0 * R1
// N = R0
// X = R1
// SUM = 0
// while N > 0
//  SUM += X
//  N--
// R2 = SUM

@R0
D=M
@n
M=D // N = R0

@R1
D=M
@x
M=D // X = R1

@sum
M=0 // SUM = 0

(ADD)
@n
D=M
@WRITE
D;JLE
@x
D=M
@sum
M=M+D // SUM += X
@n
M=M-1 // N--
@ADD
0;JMP 

(WRITE)
@sum
D=M
@R2
M=D

(END)
@END
0;JMP