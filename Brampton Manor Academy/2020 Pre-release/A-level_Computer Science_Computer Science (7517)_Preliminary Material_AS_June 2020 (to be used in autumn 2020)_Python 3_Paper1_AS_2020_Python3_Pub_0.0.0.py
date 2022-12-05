# Skeleton Program for the AQA AS1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0

EMPTY_STRING = ""
MAX_WIDTH = 100
MAX_HEIGHT = 100

class FileHeader:
  def __init__(self):
    self.Title = EMPTY_STRING
    self.Width = MAX_WIDTH
    self.Height = MAX_HEIGHT
    self.FileType = EMPTY_STRING 

def DisplayError(ErrorMessage):
  """
  Parameter: String
  Description: Takes in a string and displays an error message
  """
  print("Error: ", ErrorMessage)

def PrintHeading(Heading):
  """
  Parameters: String
  Description: Displays a heading underlined equal symbols
  """
  print(Heading)
  HeadingLength = len(Heading)
  for Position in range(1, HeadingLength + 1):
    print('=', end='')
  print()

def DisplayImage(Grid, Header):
  """
  Parameters: 2D array, Object
  Description: Prints heading and then the image
  """
  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Grid[ThisRow][ThisColumn], end='')
    print()
    
def CompressFile(Grid, Header):
  FileName = input("Enter the name of the file you want to compress: ")
  Header = FileHeader()
  FileFound = False
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileFound = True
    CompressedFile = open("CMP" + FileName + ".txt", 'w')
    Header.FileType = "C"
    HeaderLine = FileIn.readline()
    Contents = FileIn.readline()
    CompressedFile.write(HeaderLine)
    count = 1
    for i in range(len(Contents)-1):
      prev = Contents[i]
      current = Contents[i+1]
      if prev == current:
        count += 1
      else:
        CompressedFile.write(f'\n{count},{Contents[i]}')
        count = 1
  except:
    if not FileFound:
      DisplayError("File not found")
    else:
      DisplayError("Unknown error")
      
def SaveImage(Grid, Header):
  """
  Parameters: 2D array, Object
  Description: Displays the string with the header and asks the user if they want this as the filename
  """
  print("The current title of your image is: " + Header.Title)
  Answer = input("Do you want to use this as your filename? (Y/N) ")
  if Answer == "N" or Answer == "n":
    FileName = input("Enter a new filename: ")
  else:
    FileName = Header.Title
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
    FileOut.write('\n')
  FileOut.close()

def EditImage(Grid, Header):
  """
  Parameters: 2D array, Object
  Return Type: 2d array
  Description: Allows the user to edit the image by changing the symbol
  """
  DisplayImage(Grid, Header)
  Answer = EMPTY_STRING
  while Answer != "N":
    Symbol = EMPTY_STRING
    NewSymbol = EMPTY_STRING
    while len(Symbol) != 1:
      Symbol = input("Enter the symbol you want to replace: ")
    while len(NewSymbol) != 1:
      NewSymbol = input("Enter the new symbol: ")
    for ThisRow in range(Header.Height):
      for ThisColumn in range(Header.Width):
        if Grid[ThisRow][ThisColumn] == Symbol:
          Grid[ThisRow][ThisColumn] = NewSymbol
    DisplayImage(Grid, Header)
    Answer = input("Do you want to make any further changes? (Y/N) ")
  return Grid

def ConvertChar(PixelValue):
  """
  Parameters: Integer
  Return Type: String/Character
  Description: Returns a character/shade based on what integer is passed into the function
  """
  if PixelValue <= 32:
    AsciiChar = '#'
  elif PixelValue <= 64:
    AsciiChar = '&'
  elif PixelValue <= 96:
    AsciiChar = '+'
  elif PixelValue <= 128:
    AsciiChar = ';'
  elif PixelValue <= 160:
    AsciiChar = ':'
  elif PixelValue <= 192:
    AsciiChar = ','
  elif PixelValue <= 224:
    AsciiChar = '.'
  else:
    AsciiChar = ' '
  return AsciiChar

def MirrorImage(Grid, Header):
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width-1, -1 ,-1):
      print(Grid[ThisRow][ThisColumn], end='')
    print()

def FindSecretChar(PixelValue, Key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = PixelValue - Key
    if result >0 and result <27:
        return alphabet[result-1]
    elif result == 0:
        return " "
    elif result >26:
        return "_"

def LoadGreyScaleImage(FileIn, Grid, Header):
  """
  Parameters: String, 2D array, Object
  Return Type: 2D array
  Description: Returns an image by passing in the integer value of a pixel into ConvertChar and then returning the image
  """
  Key = Header.Title[-1]
  SecretMessage = ""
  try:
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        NextPixel = FileIn.readline()
        PixelValue = int(NextPixel)
        SecretMessage = SecretMessage + FindSecretChar(PixelValue, Key)
        Grid[Row][Column] = ConvertChar(PixelValue)
  except:
    DisplayError("Image data error")    
  return Grid
  
def LoadAsciiImage(FileIn, Grid, Header):
  """
  Parameters: String, 2D array, Object
  Return Type: 2D array
  Description: Takes a character in FileIn and then stores it into a pixel
  """
  try:
    ImageData = FileIn.readline()
    NextChar = 0
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        Grid[Row][Column] = ImageData[NextChar]
        NextChar += 1
  except:
    DisplayError("Image data error")
  return Grid

def LoadFile(Grid, Header):
  """
  Parameters: 2D array, Object
  Return Type: 2D array, Object
  Description: Opens file in read mode, then splits each line into fields, It passes the FileIn, Grid and Header into either LoadGreyScaleImage or LoadAsciiScaleImage depending on the file type, then it checks if the file exists, if it does then it returns the grid and Header, if not, then it prints an error message. 
  """
  FileFound = False
  FileTypeOK = False
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileFound = True
    HeaderLine = FileIn.readline()
    Fields = HeaderLine.split(',')
    Header.Title = Fields[0]
    Header.Width = int(Fields[1])
    Header.Height = int(Fields[2])
    Header.FileType = Fields[3]
    Header.FileType = Header.FileType[0]
    if Header.FileType == 'A':  
      Grid = LoadAsciiImage(FileIn, Grid, Header)
      FileTypeOK = True
    elif Header.FileType == 'G': 
      Grid = LoadGreyScaleImage(FileIn, Grid, Header)
      FileTypeOK = True
    FileIn.close()
    if not FileTypeOK:
      DisplayError("Unknown file type")
    else:
      DisplayImage(Grid, Header)
  except:
    if not FileFound:
      DisplayError("File not found")
    else:
      DisplayError("Unknown error")
  return Grid, Header

def SaveFile(Grid, Header):
  """
  Parameters: 2D array, Object
  Description: Imports a file and writes it, then splits each field with a comma and writes the grid to the file
  """
  FileName = input("Enter filename: ")
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + ',' + str(Header.Width) + ',' + str(Header.Height) + ',' + 'A' + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
  FileOut.close()

def ClearGrid(Grid):
  """
  Parameters: 2D array
  Return Type: 2D array
  Description: Replaces each pixel with .
  """
  for Row in range(MAX_HEIGHT):
    for Column in range(MAX_WIDTH):
      Grid[Row][Column] = '.'
  return Grid
   
def DisplayMenu():
  """
  Description: Prints out the menu
  """
  print()
  print("Main Menu")
  print("=========")
  print("L - Load graphics file") 
  print("D - Display image")
  print("M - Mirror image")
  print("E - Edit image")
  print("C - Compress image")
  print("S - Save image")
  print("X - Exit program") 
  print()

def GetMenuOption():
  """
  Return Type: String
  Description: Takes in the user's choice for the menu
  """
  MenuOption = EMPTY_STRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
  
def Graphics():
  """
  Description: Creates an empty grid, calls the DisplayMenu sub program to output the menu for the user, calls different functions depending on the users choice or displays an error message if they have inputted invalid arguments and finally asks the user if they want to save the file, calling the SaveFile function if yes
  """
  Grid = [['' for Column in range(MAX_WIDTH)] for Row in range(MAX_HEIGHT)]
  Grid = ClearGrid(Grid)
  Header = FileHeader()
  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      Grid, Header = LoadFile(Grid, Header)
    elif MenuOption == 'D':
      DisplayImage(Grid, Header) 
    elif MenuOption == 'M':
      MirrorImage(Grid, Header)
    elif MenuOption == 'E':
      Grid = EditImage(Grid, Header)
    elif MenuOption == 'C':
      CompressFile(Grid, Header)
    elif MenuOption == 'S':    
      SaveImage(Grid, Header)
    elif MenuOption == 'X':
      ProgramEnd = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
  Answer = input("Do you want to save the image as a graphics file? (Y/N) ")
  if Answer == "Y" or Answer == "y":
    SaveFile(Grid, Header)
      
if __name__ == "__main__":
  Graphics()         
