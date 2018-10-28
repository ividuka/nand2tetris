// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

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
@N
M=D // N = R0

@R1
D=M
@X
M=D // X = R1

@0
D=A
@SUM
M=D // SUM = 0

(ADD)
@X
D=M
@SUM
M=M+D // SUM += X
@N
M=M-1 // N--
D=M
@ADD
D;JGT 

@SUM
D=M
@R2
M=D

(END)
@END
0;JMP
