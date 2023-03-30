# Skeleton Program for the AQA AS Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0


EMPTY_STRING = ""
HI_MEM = 20
MAX_INT = 127 # 8 bits available for operand (two's complement integer)
PC = 0
ACC = 1
STATUS = 2
TOS = 3
ERR = 4

class AssemblerInstruction:
  def __init__(self):
    self.OpCode = EMPTY_STRING
    self.OperandString = EMPTY_STRING
    self.OperandValue = 0

def DisplayMenu():
  """
  Description: Displays the option menu
  """
  print()
  print("Main Menu")
  print("=========")
  print("L - Load a program file")
  print("D - Display source code")
  print("E - Edit source code")
  print("A - Assemble program")
  print("R - Run the program")
  print("X - Exit simulator") 
  print()

def GetMenuOption():
  """
  Return Type: String
  Description: Allows user to input their choice
  """
  Choice = EMPTY_STRING
  while len(Choice) != 1:
    Choice = input("Enter your choice: ")
  return Choice[0]

def ResetSourceCode(SourceCode):
  """
  Parameters: 1D Array
  Return Type: 1D Array
  Description: Resets SourceCode by making contents of every index ""
  """
  for LineNumber in range(HI_MEM):
    SourceCode[LineNumber] = EMPTY_STRING
  return SourceCode

def ResetMemory(Memory):
  """
  Parameters: 1D Array
  Return Type: 1D Array
  Description: Resets Method by resetting the attributes of each object at each index
  """
  for LineNumber in range(HI_MEM):
    Memory[LineNumber].OpCode = EMPTY_STRING
    Memory[LineNumber].OperandString = EMPTY_STRING
    Memory[LineNumber].OperandValue = 0
  return Memory

def DisplaySourceCode(SourceCode):
  """
  Parameters: 1D Array
  Description: Displays the contents of SourceCode line by line
  """
  print()
  NumberOfLines = int(SourceCode[0])
  for LineNumber in range(0, NumberOfLines + 1):
    print("{:>2d} {:<40s}".format(LineNumber, SourceCode[LineNumber]))
  print()

def LoadFile(SourceCode):
  """
  Parameters: 1D Array
  Return Type: 1D Array
  Description: Fills up SourceCode with the contents of the txt file (SourceCode[0] reserved for number of lines in txt file)
  """
  FileExists = False
  SourceCode = ResetSourceCode(SourceCode)
  LineNumber = 0
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileExists = True
    Instruction = FileIn.readline()
    while Instruction != EMPTY_STRING: 
      LineNumber += 1
      SourceCode[LineNumber] = Instruction[:-1] 
      Instruction = FileIn.readline()
    FileIn.close()
    SourceCode[0] = str(LineNumber)
  except:
    if not FileExists:
      print("Error Code 1")     #If file does not exist
    else:
      print("Error Code 2")     #If number of lines in txt file exceeds 19?
      SourceCode[0] = str(LineNumber - 1) 
  if LineNumber > 0:
    DisplaySourceCode(SourceCode)
  return SourceCode

def EditSourceCode(SourceCode):
  """
  Parameters: 1D Array
  Return Type: 1D Array
  Description: Allows the user to edit a line of their choice
  """
  LineNumber = int(input("Enter line number of code to edit: "))
  print(SourceCode[LineNumber])
  Choice = EMPTY_STRING
  while Choice != "C":
    Choice = EMPTY_STRING
    while Choice != "E" and Choice != "C":
      print("E - Edit this line")
      print("C - Cancel edit")
      Choice = input("Enter your choice: ")
    if Choice == "E":
      SourceCode[LineNumber] = input("Enter the new line: ")
    DisplaySourceCode(SourceCode)
  return SourceCode

def UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber):
  """
  Parameters: Dictionary, String, Integer
  Return Type: Dictionary
  Description: Adds new symbols with its line number/memory location
  """
  if ThisLabel in SymbolTable:
    print("Error Code 3")     #If uses same symbol,label (e.g NUM1, NUM2, WHILE)
  else:
    SymbolTable[ThisLabel] = LineNumber
  return SymbolTable

def ExtractLabel(Instruction, LineNumber, Memory, SymbolTable):
  """
  Parameters: String, Integer, 1D Array, Dictionary
  Return Type: Dictionary, 1D Array
  Description: Takes the label and uses UpdateSymbolTable to add the label to SymbolTable 
  """
  if len(Instruction) > 0: 
    ThisLabel = Instruction[0:5]
    ThisLabel = ThisLabel.strip()
    if ThisLabel != EMPTY_STRING:
      if Instruction[5] != ':':
        print("Error Code 4")     #If there is no : at 5th index of Instruction
        Memory[0].OpCode = "ERR"
      else:
        SymbolTable = UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber)
  return SymbolTable, Memory

def ExtractOpCode(Instruction, LineNumber, Memory):
  """
  Parameters: String, Integer, 1D Array
  Return Type: 1D Array
  Desription: Takes the opcode and addressing mode (if immediate) and uses them to update the current object in Memory
  """
  if len(Instruction) > 9:
    OpCodeValues = ["LDA", "STA", "LDA#", "HLT", "ADD", "JMP", "SUB", "CMP#", "BEQ", "SKP", "JSR", "RTN", "   "]
    Operation = Instruction[7:10]     #Operation = Opcode (e.g LDA, CMP), could be empty if just assigning to symbols
    if len(Instruction) > 10:
      AddressMode = Instruction[10:11]
      if AddressMode == '#':
        Operation += AddressMode
    if Operation in OpCodeValues:
      Memory[LineNumber].OpCode = Operation
    else:
      if Operation != EMPTY_STRING:
        print("Error Code 5")     #If Operation holds anything other than values in OpCodeValues or "" 
        Memory[0].OpCode = "ERR"
  return Memory   
  
def ExtractOperand(Instruction, LineNumber, Memory):
  """
  Parameters: String, Integer, 1D Array
  Return Type: 1D Array
  Description: Takes operand (uses string before * if present) and uses it to update the current object in Memory
  """
  if len(Instruction) >= 13:
    Operand = Instruction[12:] 
    ThisPosition = -1
    for Position in range(len(Operand)):
      if Operand[Position] == '*':
        ThisPosition = Position
    if ThisPosition >= 0:
      Operand = Operand[:ThisPosition]
    Operand = Operand.strip()
    Memory[LineNumber].OperandString = Operand
  return Memory

def PassOne(SourceCode, Memory, SymbolTable):
  """
  Parameters: 1D Array, 1D Array, Dictionary
  Return Type: 1D Array, Dictionary
  Description: Takes each line of code and uses subroutines to extract the label, opcode and operand
  """
  NumberOfLines = int(SourceCode[0])
  for LineNumber in range(1, NumberOfLines + 1):
    Instruction = SourceCode[LineNumber]
    SymbolTable, Memory = ExtractLabel(Instruction, LineNumber, Memory, SymbolTable)
    Memory = ExtractOpCode(Instruction, LineNumber, Memory)
    Memory = ExtractOperand(Instruction, LineNumber, Memory)
  return Memory, SymbolTable

def PassTwo(Memory, SymbolTable, NumberOfLines):
  """
  Parameters: 1D Array, Dictionary, Integer
  Return Type: 1D Array
  Description: Updates the OperandValue  attribute of the object, does nothing if Operand is an empty string
  """
  for LineNumber in range(1, NumberOfLines + 1):
    Operand = Memory[LineNumber].OperandString
    if Operand != EMPTY_STRING:
      if Operand in SymbolTable:
        OperandValue = SymbolTable[Operand]
        Memory[LineNumber].OperandValue = OperandValue
      else:
        try:
          OperandValue = int(Operand)
          Memory[LineNumber].OperandValue = OperandValue
        except:
          print("Error Code 6")
          Memory[0].OpCode = "ERR"
  return Memory

def DisplayMemoryLocation(Memory, Location):
  """
  Parameters: 1D Array, Integer
  Description: Displays the opcodes and operands of the memory locations
  """
  print("*  {:<5s}{:<5d} |".format(Memory[Location].OpCode, Memory[Location].OperandValue), end='')

def DisplaySourceCodeLine(SourceCode, Location):
  """
  Parameters: 1D Array, Integers
  Description: Displays the line number and the contents of each line number in the source code
  """
  print(" {:>3d}  |  {:<40s}".format(Location, SourceCode[Location]))

def DisplayCode(SourceCode, Memory):
  """
  Parameters: 1D Array, 1D Array
  Description: Displays the headings and uses subroutines to display 
  """
  print("*  Memory     Location  Label  Op   Operand Comment")
  print("*  Contents                    Code")
  NumberOfLines = int(SourceCode[0])
  DisplayMemoryLocation(Memory, 0)
  print("   0  |")
  for Location in range(1, NumberOfLines + 1):
    DisplayMemoryLocation(Memory, Location)
    DisplaySourceCodeLine(SourceCode, Location)

def Assemble(SourceCode, Memory):
  """
  Parameters: 1D Array, 1D Array
  Return Type: 1D Array
  Description: Updates contents of Memory and SymbolTable using subroutines
  """
  Memory = ResetMemory(Memory)
  NumberOfLines = int(SourceCode[0])
  SymbolTable = {}
  Memory, SymbolTable = PassOne(SourceCode, Memory, SymbolTable)
  if Memory[0].OpCode != "ERR":
    Memory[0].OpCode = "JMP"
    if "START" in SymbolTable:
      Memory[0].OperandValue = SymbolTable["START"]
    else:
      Memory[0].OperandValue = 1 
    Memory = PassTwo(Memory, SymbolTable, NumberOfLines)
  return Memory

def ConvertToBinary(DecimalNumber):
  """
  Parameters: Integer
  Return Type: String
  Description: Converts a denary number to binary using recursive division by 2
  """
  BinaryString = EMPTY_STRING
  while DecimalNumber > 0:
    Remainder = DecimalNumber % 2
    Bit = str(Remainder)
    BinaryString = Bit + BinaryString
    DecimalNumber = DecimalNumber // 2
  while len(BinaryString) < 3:
    BinaryString = '0' + BinaryString
  return BinaryString

def ConvertToDecimal(BinaryString):
  """
  Parameters: String
  Return Type: Integer
  Description: Converts a binary pattern into denary
  """
  DecimalNumber = 0
  for Bit in BinaryString:
    BitValue = int(Bit)
    DecimalNumber = DecimalNumber * 2 + BitValue
  return DecimalNumber

def DisplayFrameDelimiter(FrameNumber):
  """
  Parameters: Integer
  Description: Displays the delimiter between each frame
  """
  if FrameNumber == -1:
    print("***************************************************************")
  else:
    print("****** Frame",FrameNumber, "************************************************")
  
def DisplayCurrentState(SourceCode, Memory, Registers):
  """
  Parameters: 1D Array, 1D Array, 1D Array
  Description: Displays the contents of each register
  """
  print("*")
  DisplayCode(SourceCode, Memory)
  print("*")
  print("*  PC: ", Registers[PC], " ACC: ", Registers[ACC], " TOS: ", Registers[TOS])
  print("*  Status Register: ZNV")
  print("*                  ", ConvertToBinary(Registers[STATUS]))
  DisplayFrameDelimiter(-1)
  
def SetFlags(Value, Registers):
  """
  Parameters: Integer, 1D Array
  Return Type: 1D Array
  Description: Sets the status of each flag depending on the value in the Accumulator
  """
  if Value == 0:
    Registers[STATUS] = ConvertToDecimal("100")
  elif Value < 0:
    Registers[STATUS] = ConvertToDecimal("010")
  elif Value > MAX_INT or Value < -(MAX_INT + 1):
    Registers[STATUS] = ConvertToDecimal("001")
  else:
    Registers[STATUS] = ConvertToDecimal("000")    
  return Registers

def ReportRunTimeError(ErrorMessage, Registers):
  """
  Parameters: String, 1D Array
  Return Type: 1D Array
  Description: displays error message and sets ERR Register to 1
  """
  print("Run time error:", ErrorMessage)
  Registers[ERR] = 1
  return Registers
 
def ExecuteLDA(Memory, Registers, Address):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Loads Operand from the object into Accumulator and uses SetFlags to update the statuses of the flags
  """
  Registers[ACC] = Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  return Registers

def ExecuteSTA(Memory, Registers, Address):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Stores value in Accumulator into OperandValue in Memory[Address]
  """
  Memory[Address].OperandValue = Registers[ACC]
  return Memory

def ExecuteLDAimm(Registers, Operand):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Loads immediate operand into Accumulator and uses SetFlags to update the statuses of the flags
  """
  Registers[ACC] = Operand
  Registers = SetFlags(Registers[ACC], Registers)
  return Registers

def ExecuteADD(Memory, Registers, Address):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Adds OperandValue in Memory[Address] to value in Accumulator and uses SetFlags to update the statuses of the flags
  """
  Registers[ACC] = Registers[ACC] + Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  if Registers[STATUS] == ConvertToDecimal("001"):
    ReportRunTimeError("Overflow", Registers)
  return Registers

def ExecuteSUB(Memory, Registers, Address):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Subtracts OperandValue in Memory[Address] from value in Accumulator and uses SetFlags to update the statuses of the flags
  """
  Registers[ACC] = Registers[ACC] - Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  if Registers[STATUS] == ConvertToDecimal("001"):
    ReportRunTimeError("Overflow", Registers)
  return Registers

def ExecuteCMPimm(Registers, Operand):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array
  Description: Subtracts immediate operand from the value in the accumulator and uses SetFlags to update the statuses of the flags
  """
  Value = Registers[ACC] - Operand
  Registers = SetFlags(Value, Registers)
  return Registers

def ExecuteBEQ(Registers, Address):
  """
  Parameters: 1D Array, Integer
  Return Type: 1D Array
  Description: Updates the status of the registers, if flag Z is set to 1 after CMP then contents of the PC become the address
  """
  StatusRegister = ConvertToBinary(Registers[STATUS])
  FlagZ = StatusRegister[0]
  if FlagZ == "1":
    Registers[PC] = Address
  return Registers

def ExecuteJMP(Registers, Address):
  """
  Parameters: 1D Array, Integer
  Return Type: 1D Array
  Description: Changes the contents of the PC to the Address
  """
  Registers[PC] = Address
  return Registers

def ExecuteSKP():
  """
  Description: Performs the SKP instruction
  """
  return 

def DisplayStack(Memory, Registers):
  """
  Parameters: 1D Array, 1D Array
  Description: Display the Stack (Location | Stack Contents)
  """
  print("Stack contents:")
  print(" ----")
  for Index in range(Registers[TOS], HI_MEM):
    print("|{:>3d} |".format(Memory[Index].OperandValue))
  print(" ----")

def ExecuteJSR(Memory, Registers, Address):
  """
  Parameters: 1D Array, 1D Array, Integer
  Return Type: 1D Array, 1D Array
  Description: Updates StackPointer and TOS and changes the contents of the PC using Address
  """
  StackPointer = Registers[TOS] - 1
  Memory[StackPointer].OperandValue = Registers[PC] 
  Registers[PC] = Address 
  Registers[TOS] = StackPointer
  DisplayStack(Memory, Registers)
  return Memory, Registers

def ExecuteRTN(Memory, Registers):
  """
  Parameters: 1D Array, 1D Array
  Return Type: 1D Array
  Description: Updates StackPointer and TOS and changes the contents of the PC using Memory[StackPointer].OperandValue
  """
  StackPointer = Registers[TOS]
  Registers[TOS] += 1 
  Registers[PC] = Memory[StackPointer].OperandValue
  return Registers
 
def Execute(SourceCode, Memory):
  """
  Parameters: 1D Array, 1D Array
  Description: Initialises the registers and uses subroutines to perform instructions depending on the opcode
  """
  Registers = [0, 0, 0, 0, 0] 
  Registers = SetFlags(Registers[ACC], Registers)
  Registers[PC] = 0 
  Registers[TOS] = HI_MEM
  FrameNumber = 0
  DisplayFrameDelimiter(FrameNumber)
  DisplayCurrentState(SourceCode, Memory, Registers)
  OpCode = Memory[Registers[PC]].OpCode
  while OpCode != "HLT":
    FrameNumber += 1
    print()
    DisplayFrameDelimiter(FrameNumber)
    Operand = Memory[Registers[PC]].OperandValue
    print("*  Current Instruction Register: ", OpCode, Operand)
    Registers[PC] = Registers[PC] + 1
    if OpCode == "LDA":
      Registers = ExecuteLDA(Memory, Registers, Operand)
    elif OpCode == "STA": 
      Memory = ExecuteSTA(Memory, Registers, Operand) 
    elif OpCode == "LDA#": 
      Registers = ExecuteLDAimm(Registers, Operand)
    elif OpCode == "ADD":
      Registers = ExecuteADD(Memory, Registers, Operand)
    elif OpCode == "JMP": 
      Registers = ExecuteJMP(Registers, Operand)
    elif OpCode == "JSR":
      Memory, Registers = ExecuteJSR(Memory, Registers, Operand)
    elif OpCode == "CMP#":
      Registers = ExecuteCMPimm(Registers, Operand)
    elif OpCode == "BEQ":
      Registers = ExecuteBEQ(Registers, Operand) 
    elif OpCode == "SUB":
      Registers = ExecuteSUB(Memory, Registers, Operand)
    elif OpCode == "SKP":
      ExecuteSKP()
    elif OpCode == "RTN":
      Registers = ExecuteRTN(Memory, Registers)
    if Registers[ERR] == 0:
      OpCode = Memory[Registers[PC]].OpCode    
      DisplayCurrentState(SourceCode, Memory, Registers)
    else:
      OpCode = "HLT"
  print("Execution terminated")

def AssemblerSimulator():
  """
  Description: Initialises SourceCode and Memory, and runs subroutines depending on the choice the user has made in the options menu
  """
  SourceCode = [EMPTY_STRING for Lines in range(HI_MEM)]
  Memory = [AssemblerInstruction() for Lines in range(HI_MEM)]     #Each line number is an object
  SourceCode = ResetSourceCode(SourceCode)
  Memory = ResetMemory(Memory)
  Finished = False
  while not Finished:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      SourceCode = LoadFile(SourceCode)
      Memory = ResetMemory(Memory)
    elif MenuOption == 'D':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 7")
      else:
        DisplaySourceCode(SourceCode)
    elif MenuOption == 'E':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 8")
      else:
        SourceCode = EditSourceCode(SourceCode)
        Memory = ResetMemory(Memory)
    elif MenuOption == 'A':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 9")
      else:
        Memory = Assemble(SourceCode, Memory)
    elif MenuOption == 'R':
      if Memory[0].OperandValue == 0:
        print("Error Code 10")
      elif Memory[0].OpCode == "ERR":  
        print("Error Code 11")
      else:
        Execute(SourceCode, Memory) 
    elif MenuOption == 'X':
      Finished = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
      
if __name__ == "__main__":
  AssemblerSimulator()         
