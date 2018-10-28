
class CodeWriter:
    
        cnt_equal = 0
        cnt_less = 0
        cnt_greater = 0
        fileName = ""

        def __init__(self, inputFile):
            outputFile = inputFile.replace("vm","asm")
            self.file = open(outputFile, "w")
            self.fileName = inputFile.replace(".vm","")

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
        
        def writePush(self, segment, index):
            indexData = "@" + str(index) + "\nD=A\n"
            pushCommands = "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            segmentDic = {"local":"@LCL", "argument":"@ARG", "this":"@THIS", "that":"@THAT"}
            
            if segment == "constant":
                command = indexData + pushCommands
            elif segment in segmentDic.keys():
                segCommand = "\nA=M+D\nD=M\n"
                command = indexData + segmentDic.get(segment) + segCommand + pushCommands
            elif segment == "static":
                label = "@" + self.fileName + "." + str(index)
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
                label = "@" + self.fileName + "." + str(index)
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

        def close(self):
            self.file.close()