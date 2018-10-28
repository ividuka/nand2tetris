import sys

class Parser:
    currentCommand = ""
    currentType = None
    # commandTypes = ["C_ARITHMETIC","C_PUSH","C_POP","C_LABEL","C_GOTO","C_IF","C_FUNCTION","C_RETURN","C_CALL"]

    def __init__(self, inputFile):
        self.file = open(inputFile, "r")

    def hasMoreCommands(self):
        self.currentCommand = self.file.readline()
        if len(self.currentCommand) != 0:
            return True
        return False
    
    def advance(self):
        self.refineCommand()
        print(self.currentCommand)
        return self.currentCommand

    def commandType(self):
        arithmetics = ['add','sub','neg','and','or','not','eq','lt','gt']
        keyword = self.currentCommand.split()[0]

        if keyword in arithmetics:
            self.currentType = "C_ARITHMETIC"
            return
        if keyword == "push":
            self.currentType = "C_PUSH"
            return
        if keyword == "pop":
            self.currentType = "C_POP"
        
        return        

    def arg1(self):
        if self.currentType == "C_RETURN":
            argument1 = None
        elif self.currentType == "C_ARITHMETIC":
            argument1 = self.currentCommand.split()[0]
        else:
            argument1 = self.currentCommand.split()[1]
        return argument1
    
    def arg2(self):
        if self.currentType in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            argument2 = self.currentCommand.split()[2]
        else:
            argument2 = None
        return argument2

    def refineCommand(self):
        self.currentCommand = self.currentCommand.rstrip("\n")
        if self.currentCommand[:2] == "//":
            self.currentCommand = ""
