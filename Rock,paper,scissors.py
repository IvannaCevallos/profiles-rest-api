import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to my game")
        self.moves : dict = {'rock':'rock', 'paper':'paper', 'scissors':'scissors'}
        self.valid_moves : list[str] = list(self.moves.keys())
        self.userWin : int = 0
        self.aiWin : int = 0
    def play_games(self):
        user_move:str = input('Rocky, paper or Scissors>> ').lower()
        if user_move == 'exit':
            print("Thanks for playing")
            sys.exit()
        if user_move not in self.valid_moves:
            print("Ivalid name  ")
            return self.play_games()
        ai_move : str = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move:str, ai_move:str):
        print("------")
        print(f"you : {self.moves[user_move]}")
        print(f"ai : {self.moves[ai_move]}")
        print("------")

    def check_move(self,user_move:str, ai_move:str):
        if(user_move == ai_move):
            print("it is a tie")
        elif(user_move == 'rock' and ai_move == 'scissors'):
            print("You win")
            self.userWin +=1
        elif (user_move == 'scissors' and ai_move == 'paper'):
            print("You win")
            self.userWin += 1
        elif (user_move == 'paper' and ai_move == 'rock'):
            print("You win")
            self.userWin += 1
        else:
            print("HA HA HA Your loose")
            self.aiWin += 1
        print(f'The score is User: {self.userWin} vs AI: {self.aiWin}')

if __name__ == '__main__':
    rps : RPS = RPS()
    while True:

        rps.play_games()