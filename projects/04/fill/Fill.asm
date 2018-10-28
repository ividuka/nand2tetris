// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// if KBD != 0
//      go through SCREEN->KBD
//          write -1 
// else
//      go through SCREEN->KBD
//          write 0


@SCREEN
D=A
@scr
M=D // scr=16384

@KBD
D=A
@kbd
M=D // kbd=24576

(LOOP)
    @scr
    D=M
    @i
    M=D // i=scr

    @kbd
    A=M
    D=M
    @WHITE
    D;JEQ // if kbd==0 goto WHITE

    (BLACK)
        @i
        D=M
        @kbd
        D=M-D
        @LOOP
        D;JEQ // if kbd-i == 0 goto LOOP
        @i
        A=M
        M=-1 // RAM[i]=1111111111111111
        @i
        M=M+1
        @BLACK
        0;JMP     

    (WHITE)
        @i
        D=M
        @kbd
        D=M-D
        @LOOP
        D;JEQ // if kbd-i == 0 goto LOOP
        @i
        A=M
        M=0 // RAM[i]=0000000000000000
        @i
        M=M+1
        @WHITE
        0;JMP     