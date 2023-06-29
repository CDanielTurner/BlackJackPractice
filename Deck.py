import random
number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suit = ['diamonds', 'spades', 'hearts', 'clubs']

random_index = random.randrange(len(number[0:13]))
random_index2 = random.randrange(len(suit[0:4]))
popped_value1 = number.pop(random_index) + " of " + suit.pop(random_index2)
popped_value2 = number.pop(random_index) + " of " + suit.pop(random_index2)

dealer = popped_value1
player = popped_value2

#feature that the 'house' always wins, or perhaps its a bug...
def blackjack():
    print(f"your card is a", popped_value2)
    print(f"the dealers card is a", popped_value1)
    if popped_value2 > popped_value1:
        print("The dealer won....again")
    else:
        print("You win!!")

blackjack()
