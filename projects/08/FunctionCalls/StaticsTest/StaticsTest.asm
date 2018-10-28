// SP = 256
@256
D=A
@SP
M=D
// call Sys.init
// push returnAddress
@StaticsTest.vm$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-5-numArgs
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.init
0;JMP
(StaticsTest.vm$ret.0)
// function Class2.set 0
(Class2.set)
// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 0
@SP
M=M-1
@SP
A=M
D=M
@Class2.vm.0
M=D
// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 1
@SP
M=M-1
@SP
A=M
D=M
@Class2.vm.1
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// return
// endFrame = LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame-5)
@5
D=A
@endFrame
A=M-D
D=M
@retAddr
M=D
// *ARG = pop()
@0
D=A
@ARG
D=M+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@1
D=A
@endFrame
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@2
D=A
@endFrame
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@3
D=A
@endFrame
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@4
D=A
@endFrame
A=M-D
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function Class2.get 0
(Class2.get)
// push static 0
@Class2.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class2.vm.1
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
// return
// endFrame = LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame-5)
@5
D=A
@endFrame
A=M-D
D=M
@retAddr
M=D
// *ARG = pop()
@0
D=A
@ARG
D=M+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@1
D=A
@endFrame
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@2
D=A
@endFrame
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@3
D=A
@endFrame
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@4
D=A
@endFrame
A=M-D
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function Class1.set 0
(Class1.set)
// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 0
@SP
M=M-1
@SP
A=M
D=M
@Class1.vm.0
M=D
// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 1
@SP
M=M-1
@SP
A=M
D=M
@Class1.vm.1
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// return
// endFrame = LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame-5)
@5
D=A
@endFrame
A=M-D
D=M
@retAddr
M=D
// *ARG = pop()
@0
D=A
@ARG
D=M+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@1
D=A
@endFrame
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@2
D=A
@endFrame
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@3
D=A
@endFrame
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@4
D=A
@endFrame
A=M-D
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function Class1.get 0
(Class1.get)
// push static 0
@Class1.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class1.vm.1
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
// return
// endFrame = LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame-5)
@5
D=A
@endFrame
A=M-D
D=M
@retAddr
M=D
// *ARG = pop()
@0
D=A
@ARG
D=M+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@1
D=A
@endFrame
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@2
D=A
@endFrame
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@3
D=A
@endFrame
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@4
D=A
@endFrame
A=M-D
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set 2
// push returnAddress
@Sys.vm$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-5-numArgs
@5
D=A
@2
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class1.set
0;JMP
(Sys.vm$ret.0)
// pop temp 0 
@0
D=A
@5
D=A+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set 2
// push returnAddress
@Sys.vm$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-5-numArgs
@5
D=A
@2
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class2.set
0;JMP
(Sys.vm$ret.1)
// pop temp 0 
@0
D=A
@5
D=A+D
@addr
M=D
@SP
M=M-1
@SP
A=M
D=M
@addr
A=M
M=D
// call Class1.get 0
// push returnAddress
@Sys.vm$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-5-numArgs
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class1.get
0;JMP
(Sys.vm$ret.2)
// call Class2.get 0
// push returnAddress
@Sys.vm$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-5-numArgs
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class2.get
0;JMP
(Sys.vm$ret.3)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0;JMP
