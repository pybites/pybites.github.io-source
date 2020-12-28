import os

filename = 'homework.txt'

if not os.path.exists(filename):
    with open(filename, 'w'): pass

answer1 = """1). 
            X  | 3  | X
           ____|____|____
            9  | X  | 1
           ____|____|____
            2  | 7  | X
               |    |    """

answer2 = """2). 
            4  | 9  | X
           ____|____|____
            X  | X  | X
           ____|____|____
            8  | 1  | 6
               |    |    """

answer3 = """3). 
            8  | X  | 6
           ____|____|____
            X  | 5  | X
           ____|____|____
            X  | 9  | 2
               |    |    """      

answer4 = """4). 
            X  | X  | 4
           ____|____|____
            7  | 5  | 3
           ____|____|____
            X  | 1  | X
               |    |    """          

answer5 = """5). 
            2  | 7  | X
           ____|____|____
            9  | 5  | X
           ____|____|____
            X  | X  | 8
               |    |    """       

answer6 = """6). 
            X  | X  | 2
           ____|____|____
            1  | X  | X
           ____|____|____
            8  | 3  | 4
               |    |    """

answer7 = """7). 
            6  | 7  | X
           ____|____|____
            X  | 5  | X
           ____|____|____
            X  | 3  | 4
               |    |    """      

answer8 = """8). 
            x  | x  | 6
           ____|____|____
            x  | x  | 7
           ____|____|____
            x  | 9  | 2
               |    |    """   

answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7]
numbers = [['4','8','5','6'],
           ['2','3','5','7'],
           ['1','3','7','4'],
           ['2','9','6','8'],
           ['6','1','4','3'],
           ['6','7','5','9'],
           ['2','1','9','8']]


def substitute(problems, numbers):
   """since str.replace() replaces all instances
   at once, I had to resort to some manipulation to replace each X."""
   k = 0
   final_answers = []

   for i in range(len(problems)):
      problem = problems[i]
      for j in range(len(problem)):
         if problem[j] == 'X':
            problem = list(problem)
            problem[j] = numbers[i][k]
            problem = ''.join(problem)
            k += 1
            if k == 4:
               k = 0
      
      final_answers.append(problem)
      
   return final_answers


def write_to_file(infile):
   with open(infile, 'w') as f:
      f.write('MAGIC SQUARES\n\n')
      for answer in substitute(answers,numbers):
         f.write(answer + '\n\n')
      f.write(answer8)


if __name__ == '__main__':
   write_to_file(filename)