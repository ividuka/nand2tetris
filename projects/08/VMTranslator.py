import sys
import os
import parser as ps
import codeWriter as cw

def translateVm(myParser, myWriter):
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
        elif type == "C_LABEL":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeLabel(arg1)
        elif type == "C_GOTO":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeGoto(arg1)
        elif type == "C_IF":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeIf(arg1)
        elif type == "C_CALL":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeCall(arg1, arg2)
        elif type == "C_FUNCTION":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeFunction(arg1, arg2)
        elif type == "C_RETURN":
            myWriter.writeVMCommand(myParser.currentCommand)
            myWriter.writeReturn()                  
              

def main(argv):
    inputName = argv[0]

    if os.path.isdir(inputName):
        outputPath = inputName
        print(outputPath)
        outputFile = os.path.basename(outputPath)
        myWriter = cw.CodeWriter(outputPath + "/" + outputFile)
        myWriter.setFileName(outputFile + ".vm")
        myWriter.writeInit()
        for filename in os.listdir(inputName):
            if filename.endswith(".vm"):
                myParser = ps.Parser(inputName + "/" + filename)
                myWriter.setFileName(filename)
                translateVm(myParser, myWriter)
        myWriter.close()       
    elif inputName.endswith(".vm"):
        myParser = ps.Parser(inputName)
        outputFile = inputName.replace(".vm","")
        myWriter = cw.CodeWriter(outputFile)
        myWriter.setFileName(inputName)
        translateVm(myParser, myWriter)
        myWriter.close()

if __name__ == '__main__':
    main(sys.argv[1:])
