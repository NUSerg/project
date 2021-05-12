import random
import time

class color:
  Red = '\033[91m'
  Green = '\033[92m'
  Blue = '\033[94m'
  BOLD = '\033[1m'
  END = '\033[0m'

print(f'{color.Green}{color.BOLD}Игра "Камень, ножницы, бумага"{color.END}')
a = input(f'{color.Green}Для того чтобы начать игру нажми: {color.Blue}пробел\n')

if a == ' ':
  run = True
  print(f'{color.Green}Игра началась\nИграем до трёх')
else:
  print('Ну не хочь, как хочь!')
  run = False

list = ['к', 'н', 'б']
player = 0
computer = 0  
while run:
  if player < 3 and computer < 3:
    comp = random.choice(list)
    choice = input(f'Выбери что-нибудь:\n{color.Blue}К{color.Green} - камень\n{color.Blue}Н{color.Green} - ножницы\n{color.Blue}Б{color.Green} - бумага\n')
    if choice.lower() == comp:
      print('Ничья, играем дальше')
      time.sleep(.5)
    elif choice.lower() == 'к' and comp == 'н':
      print('Твоя взяла')
      player += 1
      time.sleep(.5)
    elif choice.lower() == 'к' and comp == 'б':      
      print('Моя взяла')
      computer += 1
      time.sleep(.5)
    elif choice.lower() == 'н' and comp == 'б':
      print('Твоя взяла')
      player += 1
      time.sleep(.5)
    elif choice.lower() == 'н' and comp == 'к':
      print('Моя взяла')
      computer += 1
      time.sleep(.5)
    elif choice.lower() == 'б' and comp == 'к':
      print('Твоя взяла')
      player += 1
      time.sleep(.5)
    elif choice.lower() == 'б' and comp == 'н':
      print('Моя взяла')
      computer += 1
      time.sleep(.5)
    else:
      print('Ты нажал какую-то фигню')
      time.sleep(.5)
  else:
    run = False
    if player > computer:
      print(f'Ну ты красаучег, выиграл меня со счётом {color.Red}{player}{color.Green} : {color.Red}{computer}{color.Green}')
      time.sleep(2)
      b = input(f'Хочешь повторить игру?\nЕсли да то жми: {color.Blue}пробел{color.Green}\n')
      if b == ' ':
        player = 0
        computer = 0
        run = True
      else:
        print('Ну не хочь, как хочь!')
    else:
      print(f'Ну ты и лошара:), я тебя насадил со счётом {color.Red}{computer}{color.Green} : {color.Red}{player}{color.Green}')
      time.sleep(2)
      b = input(f'Хочешь повторить игру?\nЕсли да то жми: {color.Blue}пробел{color.Green}\n')
      if b == ' ':
        player = 0
        computer = 0
        run = True
      else:
        print('Ну не хочь, как хочь!')
