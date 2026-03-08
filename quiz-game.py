score = 0
print('Welcome to the Quiz Game!')
print()
q1 = input('What is the capital of India?')
if q1.lower() == 'delhi':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Delhi.')
print()
q2 = input('What is the largest planet in our solar system?')
if q2.lower() == 'jupiter':
    print('Correct!')
    score += 1
else:
    print('wrong! The correct answer is Jupiter.')
print()
q3 = input('which programming language is known as the language of the web?')
if q3.lower() == 'javascript':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is JavaScript.')
print()
print('Your final score is:', score, 'out of 3.')