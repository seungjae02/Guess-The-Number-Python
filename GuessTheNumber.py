import random
from numbers import numbers

guessednums = []

def get_num():
    randnum = int(random.choice(numbers))  # pulls out random number from number bank
    return (randnum)

def play():
    realnum = int(get_num())
    while True:
        try:
            guess = int(input('please input a number between 0 and 20: '))
        except:
            print('Invalid input. Try again.')
            continue

        if guess in guessednums:
            print('You already guessed the number', guess, '... guess again')
        elif guess <= realnum-5 and guess >= realnum-20:
            print('Your guess is pretty off from the right number. Please try again')
            guessednums.append(guess)
        elif guess < realnum and guess > realnum-5:
            print('Your guess is pretty close to the right number! Keep going!')
            guessednums.append(guess)
        elif guess >= realnum+5 and guess <= realnum+20:
            print('Your guess is pretty off from the right number. Please try again')
            guessednums.append(guess)
        elif guess > realnum and guess < realnum+5:
            print('Your guess is pretty close to the right number! Keep going!')
            guessednums.append(guess)
        elif guess == realnum:
            print('Congrats! You guessed the right number, which was', guess)
            break
    askreplay()

def askreplay():
    replay = input('Would you like to play again? If yes, input "y". If no, input "n": ')
    if replay == 'y':
        print("Alright! Let's go!")
        list.clear(guessednums)
        play()
    elif replay == 'n':
        print('Thanks for playing!')
        quit()

askplay = input('Would you like to play a game of guess the number? If yes, input "y". If no, input "n": ')
if askplay == 'y':
    get_num()
    play()
elif askplay == 'no':
    print('Okay! Have a nice day!')
    quit()
