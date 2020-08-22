import random
import colorama
name = input('enter your name : ')
print('Hello'+ ' '+ name.capitalize()+' Enjoy the Game')

def main():
    global display
    global guess_word
    global count
    global guess_length
    global words
    words= ['bird','animal','health','building','fruit','hello']
    guess_word = random.choice(words)
    guess_length  = len(guess_word)
    display = '-'* guess_length
    count =0
def Play_loop():
    replay = input(colorama.Fore.WHITE+'do you wanna play again (y for yes or n for no) : ')
    if replay.lower() == 'y' :
        main()
    elif replay.lower() == 'n':
        exit()
    else :
        print('enter a valid entry y or n')
        Play_loop()
def hangman():
    global words
    global display
    global guess_word
    global count
   
    limit = 5
    ask = input(colorama.Fore.BLUE+'this is the {} letters word '.format(guess_length)+ display+' enter the guessed letter  : ')
    if len(ask) == 0 or len(ask)>=2:
        print('invalid entry')

    elif ask in guess_word:
        index = guess_word.find(ask)
        guess_word = guess_word[:index] + '-'+ guess_word[index + 1:]
        display = display[:index] +ask+ display[index + 1:]
        print(colorama.Fore.CYAN+'correct letter in "{}" '.format(display) )
    
    else:
        count +=1
        if count == limit:
            print(colorama.Fore.RED+'you lose')
            Play_loop()
        else :print(colorama.Fore.YELLOW +'Try another letter remaining guesses is {} '.format(limit-count))
        hangman()
    if guess_word == '-' * guess_length:
        print(colorama.Fore.GREEN+'Congratulation you guessed the word " {} "'.format(display))
        Play_loop()
    elif count != limit:
        hangman()
  
   
    
main()   
hangman() 
