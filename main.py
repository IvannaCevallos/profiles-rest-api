import random
from multiprocessing.managers import Value


def roll_dice(ammount : int = 2)->tuple [ list[int], int]:
    if ammount <= 0 :
        raise Value
    rolls: list[int] = []
    sum: int = 0
    for i in range(ammount):
        random_roll : int = random.randint(1,6)
        rolls.append(random_roll)
        sum += random_roll
    return rolls, sum
def main():
    while True:
        try:
            user_input :str = input("How many dice would you like to roll ")
            if user_input.lower() == "x":
                print("Thanks for playing")
                break
            rolls, sum = roll_dice(int(user_input))
            #print(*roll_dice(int(user_input)), sep=' - ')
            print(f"Rolls {rolls}")
            print(f"sum {sum}")
        except ValueError as e:
            print(f"I dont understand {e}")
main()