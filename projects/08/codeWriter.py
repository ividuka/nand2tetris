import os

class CodeWriter:
    
        cnt_equal = 0
        cnt_less = 0
        cnt_greater = 0
        cnt_pushlcl = 0
        outputFileName = ""
        inputFileName = ""
        retAddrCounters = {}

        def __init__(self, fileName):
            self.outputFileName = os.path.basename(fileName)
            outputFile = fileName + ".asm"
            self.file = open(outputFile, "w")

        def writeArithmetic(self, command):
            print(command)
            moveSP = "@SP\nM=M-1\nA=M\nD=M\n" # SP--; D = *SP
            # pointerValue = "A=M\nD=M\n" # D = *SP
            goBeforeSP = "@SP\nA=M-1\n"
            if command == "add":
                self.file.write(moveSP + goBeforeSP + "M=M+D\n")
            elif command == "sub":
                self.file.write(moveSP + goBeforeSP + "M=M-D\n") 
            elif command == "neg":
                self.file.write(goBeforeSP + "M=-M\n")
            elif command == "and":
                self.file.write(moveSP + goBeforeSP + "M=M&D\n")
            elif command == "or":
                self.file.write(moveSP + goBeforeSP + "M=M|D\n")
            elif command == "not":
                self.file.write(goBeforeSP + "M=!M\n")
            elif command == "eq":
                self.file.write(moveSP + goBeforeSP + "D=M-D\n@EQUAL" + str(self.cnt_equal) + "\nD;JEQ\n" + goBeforeSP + "M=0\n@ENDEQ" + str(self.cnt_equal) + "\n0;JMP\n(EQUAL" + str(self.cnt_equal) + ")\n" + goBeforeSP + "M=-1\n(ENDEQ" + str(self.cnt_equal) + ")\n")
                self.cnt_equal = self.cnt_equal + 1
            elif command == "lt":
                self.file.write(moveSP + goBeforeSP + "D=M-D\n@LESS" + str(self.cnt_less) + "\nD;JLT\n" + goBeforeSP + "M=0\n@ENDLT" + str(self.cnt_less) + "\n0;JMP\n(LESS" + str(self.cnt_less) + ")\n" + goBeforeSP + "M=-1\n(ENDLT" + str(self.cnt_less) + ")\n")
                self.cnt_less = self.cnt_less + 1
            elif command == "gt":
                self.file.write(moveSP + goBeforeSP + "D=M-D\n@GREATER" + str(self.cnt_greater) + "\nD;JGT\n" + goBeforeSP + "M=0\n@ENDGT" + str(self.cnt_greater) + "\n0;JMP\n(GREATER" + str(self.cnt_greater) + ")\n" + goBeforeSP + "M=-1\n(ENDGT" + str(self.cnt_greater) + ")\n")                                   
                self.cnt_greater = self.cnt_greater + 1
            else:
                print("Command " + command + " is not supported!\n")
                self.file.close()

        def writePushPop(self, commandType, segment, index):
            print(commandType)
            if commandType == "C_PUSH":
                self.writePush(segment, index)
            elif commandType == "C_POP":
                self.writePop(segment, index)
        
        def getPushCommands(self):
            return "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        
        def writePush(self, segment, index):
            indexData = "@" + str(index) + "\nD=A\n"
            pushCommands = self.getPushCommands()
            segmentDic = {"local":"@LCL", "argument":"@ARG", "this":"@THIS", "that":"@THAT"}
            
            if segment == "constant":
                command = indexData + pushCommands
            elif segment in segmentDic.keys():
                segCommand = "\nA=M+D\nD=M\n"
                command = indexData + segmentDic.get(segment) + segCommand + pushCommands
            elif segment == "static":
                label = "@" + self.inputFileName + "." + str(index) # do they all use same name - no 
                segCommand = label + "\nD=M\n"
                command = segCommand + pushCommands
            elif segment == "temp":
                segCommand = "@5\nA=A+D\nD=M\n"
                command = indexData + segCommand + pushCommands
            elif segment == "pointer":
                label = ""
                if index == "0":
                    label = "@THIS"
                elif index == "1":
                    label = "@THAT"
                segCommand = label + "\nD=M\n"
                command = segCommand + pushCommands                    

            self.file.write(command)
        
        def writePop(self, segment, index):
            print("seg: "  + segment)
            print("index: " + index)
            indexData = "@" + str(index) + "\nD=A\n"
            popCommands = "@SP\nM=M-1\n@SP\nA=M\nD=M\n"
            segmentDic = {"local":"@LCL", "argument":"@ARG", "this":"@THIS", "that":"@THAT"}

            if segment in segmentDic.keys():
                segCommand = "\nD=M+D\n"
                command = indexData + segmentDic.get(segment) + segCommand + "@addr\nM=D\n" + popCommands + "@addr\nA=M\nM=D\n" 
            elif segment == "static":
                label = "@" + self.inputFileName + "." + str(index) # do they all use same name
                segCommand = label + "\nM=D\n"
                command = popCommands + segCommand
            elif segment == "temp":
                segCommand = "@5\nD=A+D\n"               
                command = indexData + segCommand + "@addr\nM=D\n" + popCommands + "@addr\nA=M\nM=D\n"
            elif segment == "pointer":
                label = ""
                if index == "0":
                    label = "@THIS"
                elif index == "1":
                    label = "@THAT"
                segCommand = label + "\nM=D\n"
                command = popCommands + segCommand                               

            self.file.write(command)

        def writeVMCommand(self, command):
            self.file.write("// " + command + "\n")
        
        def setFileName(self, fileName):
            self.inputFileName = fileName
            self.retAddrCounters.update({fileName:0}) 

        def writeInit(self):
            # bootstrap code?
            #SP = 256
            setSP = "@256\nD=A\n@SP\nM=D\n"
            self.file.write(setSP)
            #Call Sys.init 0
            self.writeCall("Sys.init", "0")
            
        def getJmpCommand(self, label, value):
            return "@" + label + "\n"+ value + ";JMP\n"
        
        def writeLabel(self, label):
            command = "(" + label + ")\n"
            self.file.write(command)
        
        def writeGoto(self, label):
            command = self.getJmpCommand(label, "0")
            self.file.write(command)

        def writeIf(self, label):
            popStackValue = "@SP\nM=M-1\n@SP\nA=M\nD=M\n"
            command = popStackValue + "@" + label + "\nD;JNE\n"
            self.file.write(command)
        
        def updateCounter(self):
            self.retAddrCounters[self.inputFileName] += 1
        
        def pushSegmentAddress(self, segment):
            # @segment; D=M; @SP; A=M; M=D; @SP; M=M+1 
            return "@" + segment + "\nD=M\n" + self.getPushCommands() 

        def writeCall(self, functionName, numArgs):
            # push returnAddress -> generate addr "fileName$ret.cnt"
            returnAddress = self.inputFileName + "$ret." + str(self.retAddrCounters[self.inputFileName])
            self.file.write("@" + returnAddress + "\nD=A\n" + self.getPushCommands())
            # push LCL -> call pushSegmentAddress
            self.file.write(self.pushSegmentAddress("LCL"))
            # push ARG  //same
            self.file.write(self.pushSegmentAddress("ARG"))
            # push THIS  //same
            self.file.write(self.pushSegmentAddress("THIS"))
            # push THAT  //same
            self.file.write(self.pushSegmentAddress("THAT"))
            # ARG = SP-5-numArgs -> set new value -> @5;D=A;@numArgs;D=D-A;@SP;D=M-D;@ARG;M=D
            setArg = "@5\nD=A\n@" + numArgs + "\nD=D+A\n@SP\nD=M-D\n@ARG\nM=D\n"
            self.file.write(setArg)
            # LCL = SP -> set new value -> @SP;D=M;@LCL;M=D
            setLcl = "@SP\nD=M\n@LCL\nM=D\n"
            self.file.write(setLcl)
            # goto functionName -> call getJmpCommand -> getJmpCommand(functionName,"0")
            self.file.write(self.getJmpCommand(functionName, "0"))
            # (returnAddress) -> write generated addr -> (retAddrCounters[self.inputFileName])
            self.file.write("(" + self.inputFileName + "$ret." + str(self.retAddrCounters[self.inputFileName]) + ")\n")
            # decrease cnt -> updateCounter()
            self.updateCounter()
        
        def writeFunction(self, functionName, numArgs):
            functionDeclaration = "(" + functionName + ")\n"
            setCnt = "@" + numArgs + "\nD=A\n@CNTLCL\nM=D\n" 
            label = "PUSHLCL" + str(self.cnt_pushlcl)
            pushLocalVars = "@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@CNTLCL\nM=M-1\nD=M\n@" + label + "\nD;JGT\n"
            #self.file.write(functionDeclaration + setCnt + "(" + label + ")\n" + pushLocalVars)
            self.file.write(functionDeclaration)
            for i in range(0, int(numArgs)):
                print("          EEEJJJJJ ")
                self.writePush("constant", 0)

        def setValue(self, old, offset, new):
            return "@" + str(offset) + "\nD=A\n@" + old + "\nA=M-D\nD=M\n@" + new + "\nM=D\n"   
        
        def writeReturn(self):
            # endFrame = LCL
            c = "@LCL\nD=M\n@endFrame\nM=D\n"
            self.file.write(c)
            # retAddr = *(endFrame-5)
            # @5;D=A;@endFrame;A=M-D;D=M;@retAddr;M=D
            c = self.setValue("endFrame", 5, "retAddr")
            self.file.write(c)
            # *ARG = pop()
            # @SP;A=M;D=M;@ARG;A=M;M=D
            #c = c + "@SP\nA=M\nD=M\n@ARG\nA=M\nM=D\n"
            self.writePop("argument","0")
            # SP = ARG + 1
            c = "@ARG\nD=M\n@SP\nM=D+1\n"
            # THAT = *(endFrame-1)
            c = c + self.setValue("endFrame", 1, "THAT")
            # THIS = *(endFrame-2)
            c = c + self.setValue("endFrame", 2, "THIS")
            # ARG = *(endFrame-3)
            c = c + self.setValue("endFrame", 3, "ARG")
            # LCL = *(endFrame-4)
            c = c + self.setValue("endFrame", 4, "LCL")
            # goto retAddr
            c = c + "@retAddr\nA=M\n0;JMP\n"
            self.file.write(c)

        def close(self):
            self.file.close()