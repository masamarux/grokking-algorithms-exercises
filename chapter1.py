import math

question_answer_dict = {
  '1.1': f'Doing a binary search in a list of 128 names, it will run {math.log2(128)} steps',
  '1.2': f'Doing a binary search in a list of 256 names, it will run {math.log2(256)} steps',
  '1.3': 'O(log n)',
  '1.4': 'O(n)',
  '1.5': 'O(n)',
  '1.6': 'O(n)',
}

for question, answer in question_answer_dict.items():
  print(f'Question {question}: {answer}')