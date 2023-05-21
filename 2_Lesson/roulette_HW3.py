## HW3 ##
# Casino roulette wheel:
# Rules:
#   your start Balance is 10EUR
#
#   choose a color: Black, Red or Green
#   then the roullete is gonna be rotating..
#
#   there are 38 cells:
#       18 Black Cells  - Win +2EUR
#       18 Red Cells    - Win +2EUR
#       2  Green cells  - Win +10EUR
#       Lose - 2Eur

import random


class WheelRoulette:
    total_amount = 10  # starts from 10EUR
    rounds = 1
    # 1 - Black, 2 - Red, 3 - Green
    COLORS_LIST = (1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
                   2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3)

    def __init__(self, subject) -> None:
        self.subject = subject
        self.next = None
        self.colorChoice = None
        print(self)
        self.playing()

    def __str__(self) -> str:
        return f"--------------------------\n" +\
               f"{self.subject}\n" +\
               f"--------------------------\n"

    def playing(self):
        WheelRoulette.rounds += 1

        if WheelRoulette.rounds == 2:  # 1st node number

            self.user_choice()  # user made a decision
            self.get_roullete_response()

            # Calling the next node
            self.next = WheelRoulette(f"Round nr {WheelRoulette.rounds}")
        else:  # 2nd or greater node number
            answer = input("Do you want to play again?  yes/no    ")

            if answer == 'yes':
                self.user_choice()  # user made a decision
                self.get_roullete_response()

                # Calling the next node
                self.next = WheelRoulette(f"Round nr {WheelRoulette.rounds}")
            if answer == 'no':
                print(
                    f"Thanks and see you next time, you balance is: {WheelRoulette.total_amount}EUR")

    def user_choice(self):
        while True:
            print("Choose a color from the list:")
            print("\t1   for Black cell")
            print("\t2   for Red cell")
            print("\t3   for Green cell")
            answer = input("Player choice: ")
            if answer == '1' or answer == '2' or answer == '3':
                self.colorChoice = int(answer)
                break
            elif answer == 'q':
                break
            else:
                print("Unknown Respone, try again or press 'q' to quite")

    def get_roullete_response(self):
        print("rotating the roulette...")
        result = random.choice(WheelRoulette.COLORS_LIST)
        print("roulette result is: ", result)
        if (result == self.colorChoice):
            if result == 3:
                WheelRoulette.total_amount += 10
            else:
                WheelRoulette.total_amount += 2

            print(
                f"You Won, your new balance is {WheelRoulette.total_amount}EUR")
        else:
            WheelRoulette.total_amount -= 2

            print(
                f"You Lose, your new balance is {WheelRoulette.total_amount}EUR")


player = WheelRoulette("Welcome to Casino-Royal, ROUND 1")
