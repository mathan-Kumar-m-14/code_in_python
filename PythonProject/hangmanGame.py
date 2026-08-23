import random
animalsList=['lion','tiger','cat','dog']
word=random.choice(animalsList)
print(f'Randomly selected word is : {word}')
guessed=[]
wrong_guess=0
max_attempts=6
while wrong_guess < max_attempts:
    display=''
    for letter in word:
        if letter in guessed:
            display +=letter + ' '
        else:
            display+='_'
    print('word:',display)
    if '_' not in display:
        print('Congratulation you won')
        break

    guess=input('Enter the animal name: ')

    if len(guess)!=1 or not guess.isalpha():
        print('Enter a valid character')
        continue
    if guess in guessed:
        print('Already this word is entered')
        continue

    guessed.append(guess)

    if guess in word:
        print('Entered value is match with the word')
    else:
        print('Entered a wrong value')
        wrong_guess+=1




