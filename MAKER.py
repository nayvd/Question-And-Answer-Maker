question_chooser = input('Choose a question: ')
answer_chooser = input('Choose a answer: ')

question = input(question_chooser)
if question == answer_chooser:
    print('Correct!')

else:
    print('Incorrect the answer was ' + answer_chooser + '!')
