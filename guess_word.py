import random

class color:
  Red = '\033[91m'
  Green = '\033[92m'
  Blue = '\033[94m'
  BOLD = '\033[1m'
  END = '\033[0m'

def get_word():
  word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец', 'проблема', 'час', 'право', 'нога', 'решение']
  return random.choice(word_list).upper()

def display_hangman(tries):
  stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
  return stages[tries]

def play(word):
  word_completion = '_' * len(word)
  guessed = True
  guessed_letters = []
  guessed_words = []
  tries = 6
  print(color.Green + color.BOLD + 'Игра "Угадайка слов"\n' + color.END + color.Green)
  print(color.Red + display_hangman(6) + color.Green)
  print(word_completion)
  print(f'Слово из {len(word)} букв')
  while guessed:
    answer = input('Выбери любую букву\nили укажи слово целиком\n').upper()
    if answer == word:
      print('Ты угадал слово!\nмои поздравления')
      guessed_words.append(word)
      again = input('Ещё играем? Если да, то жми пробел\n')
      if again == ' ':
        play(get_word())
      elif again != ' ':
        print('ОК, до скорой встречи!')
        guessed = False
    elif len(answer) > 1 and len(answer) < len(word):
      print('Вводить нужно только то что просят')
    elif answer in guessed_letters:
      print('Ты уже называл такую букву')
    elif answer in guessed_words:
      print('Это слово уже было')
    elif len(answer) == 1 and answer.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
      print('Вводить нужно буковки\nпричём только кириллицей')
    elif answer in word:
      print('Есть такая буква')
      guessed_letters.append(answer)
      word1 = [i for i in word_completion]
      for i in range(len(word)):
        if answer == word[i]:
          del word1[i]
          word1.insert(i, answer)
      word_completion = ''.join(word1)
      print(word_completion)
      if word_completion == word:
        print('Мои поздравления, ты отгадал это слово!!!')
        again = input('Ещё играем? Если да, то жми пробел\n')
        if again == ' ':
          play(get_word())
        elif again != ' ':
          print('ОК, до скорой встречи!')
          guessed = False
    elif answer not in word and len(answer) == 1:
      guessed_letters.append(answer)
      print('Ты не угадал букву')
      tries -= 1
      print(color.Red + display_hangman(tries) + color.Green)
      if tries == 0:
        guessed = False
        print('Ты проиграл\nтебя повесили\nлошара:)')
        again = input('Ещё играем? Если да, то жми пробел\n')
        if again == ' ':
          play(get_word())
        elif again != ' ':
          print('ОК, до скорой встречи!')
          guessed = False
    elif len(answer) == len(word) and answer != word:
      guessed_words.append(answer)
      print('Ты не угадал слово')
      tries -= 1
      print(color.Red + display_hangman(tries) + color.Green)
      if tries == 0:
        guessed = False
        print('Ты проиграл\nтебя повесили\nлошара:)')
        again = input('Ещё играем? Если да, то жми пробел\n')
        if again == ' ':
          play(get_word())
        elif again != ' ':
          print('ОК, до скорой встречи!')
          guessed = False

play(get_word())
