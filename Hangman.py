import random
Words = ['apple', 'kiwi', 'calculator', 'project', 'cunt', 'wordle']
X = random.randrange(0, 6)
length = len(Words[X])
print(f'The length of your word is {length}')
lives = 0
list_for_the_word = []

for i in range(len(Words[X])):
    list_for_the_word.append('_')

confirmation = []
for i in range(length):
    confirmation.append(Words[X][i])
end = True

while lives < 5 and end:
    print(list_for_the_word)
    guess = input('Make a guess:').lower()
    if guess in list_for_the_word:
        print('You already guessed that.')
        lives+=1
        print(f'You have {5-lives} lives remaining.')

    elif guess in Words[X]:
        print(f'{guess} is in the word.')
        for h in range(length):
            if guess == Words[X][h]:
                list_for_the_word[h] = guess
            if list_for_the_word == confirmation:
                print(f'YOU GUESSED THE WORD AND IT WAS {Words[X].upper()}')
                end = False
    else:
        print(f'{guess} is not in this word.')
        lives = lives+1
        print(f'You have {5 - lives} lives remaining.')
        if lives == 5:
            print(f'You ran out of lives. {Words[X].title()} was the word')
