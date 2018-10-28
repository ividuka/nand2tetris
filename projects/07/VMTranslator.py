import sys
import parser as ps
import codeWriter as cw

def main(argv):
    inputFile = argv[0]
    myParser = ps.Parser(inputFile)
    myWriter = cw.CodeWriter(inputFile)

    while myParser.hasMoreCommands():
        cmd = myParser.advance()
        if len(cmd)==0:
            continue
        myParser.commandType()
        type = myParser.currentType
        arg1 = myParser.arg1()
        arg2 = myParser.arg2()
        
        if type == "C_ARITHMETIC":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeArithmetic(arg1)
        elif type in ["C_PUSH", "C_POP"]:
            myWriter.writeVMCommand(myParser.currentCommand)            
            myWriter.writePushPop(type, arg1, arg2)
        
    myWriter.close()

if __name__ == '__main__':
    main(sys.argv[1:])
