// function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
@CNTLCL
M=D
(PUSHLCL0)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@CNTLCL
M=M-1
D=M
@PUSHLCL0
D;JGT
// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M+D
// not
@SP
A=M-1
M=!M
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
// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M+D
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
// sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
// return
@LCL
D=M
@endFrame
M=D
@5
D=A
@endFrame
A=M-D
D=M
@retAddr
M=D
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
@ARG
D=M
@SP
M=D+1
@1
D=A
@endFrame
A=M-D
D=M
@THAT
M=D
@2
D=A
@endFrame
A=M-D
D=M
@THIS
M=D
@3
D=A
@endFrame
A=M-D
D=M
@ARG
M=D
@4
D=A
@endFrame
A=M-D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP