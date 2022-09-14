def main():
  print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
  answer = int(input("*You* This will be the answer. Select a number between 10-49: "))
  number = int(input("*Player* Pick any number 50-99: "))
  result = calculation(answer, number)
  print("I said the answer was",answer,"and the calculation result is",result)

def calculation(answer, number):
  factor = 99 - answer
  add = factor + number
  if add > 100:
    result = number-(add - 100 + 1)
  else:
    result = number - add
  return result
  
main()
  