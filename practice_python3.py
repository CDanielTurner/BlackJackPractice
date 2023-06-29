import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suit = ['diamonds', 'spades', 'hearts', 'clubs']

random_number = random.choice(number)
random_suit = random.choice(suit)
random_number2 = random.choice(number)
random_suit2 = random.choice(suit)
random_number3 = random.choice(number)
random_suit3 = random.choice(suit)
random_number4 = random.choice(number)
random_suit4 = random.choice(suit)

player_score = random_number + random_number2
dealer_score = random_number3 + random_number4

def blackjack():
    print(f"You have a {random_number} of {random_suit} and a {random_number2} of {random_suit2}")
    print(f"{player_score}")
    print(f"The dealer has a {random_number3} of {random_suit3} and a {random_number4} of {random_suit4}")
    print(f"{dealer_score}")

while player_score <= 17:
    print(f"{player_score}")
    player_score = random_number + player_score

blackjack()