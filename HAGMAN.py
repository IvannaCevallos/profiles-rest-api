from random import choice
def run_game():
    word: str = choice(['apple', 'secret', 'apple'])
    username : str = input("What is you name: ")
    print(f"Welcome, vilkommen {username} ")
    guessed : str=''
    tries : int = 3
    while tries > 0 :
        blanks : int = 0
        print('Word: ', end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print('_', end='')
                blanks+=1
        print()
        if blanks == 0:
            print(" you guessed it")
            break
        guess : str = input("Enter a letter")
        if len(guess)>1:
            if guess in word :
                print("You are so clever, it ends prematurely")
                break
            else:
                print("Not so fast smarty pants, you loose for that")
                break
        print(guessed)
        if guess in guessed:
            print(f"you already used {guess}")
        guessed += guess
        if guess not in word:
            tries -=1
            print(f"sorry worng, {tries} remaining")
            if tries == 0:
                print("you loose")
                break
if __name__ == '__main__':
    run_game()