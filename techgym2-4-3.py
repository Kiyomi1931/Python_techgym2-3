import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  question = data[choice_data]
  print(question)

  tate=0
  yoko=0

  while tate<3:
    question_str=''
    while yoko<3:
      question_str+=question[0]
      yoko+=1
    print(question_str)
    yoko=0
    tate+=1

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()