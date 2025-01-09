import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self):
        self.name = random.choice(CARDS)
        self.value = None

def card_math(cards: list[Card], total: int = 0, seen_ace = False) -> tuple[int, bool]:
    for card in cards:
        if card.name == 'Jack' or card.name == 'Queen' or card.name == 'King':
            card.value = 10
        elif card.name == "Ace":
            card.value = 11
            seen_ace = True
        else:
            card.value = card.name
        total += card.value
    
    if total > 21 and seen_ace:
        total -= 10
    
    return total, seen_ace
        

def play_game() -> None:
    user_card1 = Card()
    user_card2 = Card()
    user_total, user_ace = card_math([user_card1, user_card2])
    
    com_card1 = Card()
    com_card2 = Card()
    com_total, com_ace = card_math([com_card1, com_card2])
    
    user_msg = f"Your cards are: {user_card1.name} and {user_card2.name}. This adds up to {user_total}"
    print(user_msg)
    
    com_msg = f"Your opponent has a {com_card2.name}"
    print(com_msg)
    
    while True:
        user_input = input("Would you like to hit? (y/n) ").lower()
        if user_input == 'n':
            break
        elif user_input == 'y':
            new_card = Card()
            user_total, user_ace = card_math([new_card], user_total, user_ace)
            print(f"You drew a {new_card.name}. User total: {user_total}")
            if user_total >= 21:
                break
        else:
            print("That is not a valid answer.")
                    
    if user_total > 21:
        print("You busted. Game Over!")
    elif user_total == 21:
        print("Blackjack! You win!!")
    else:
        print(f"The second card is a {com_card1.name}. Computer total: {com_total}")
        while com_total <= 16:
            new_card = Card()
            com_total, com_ace = card_math([new_card], com_total, com_ace)
            print(f"The computer drew a {new_card.name}. Computer total: {com_total}")
        
        if com_total == user_total:
            print(f"The computer and user both have {user_total}. This is a push!")
        elif com_total > user_total:
            print(f"The computer outscored you {com_total} to {user_total}. Computer wins!")
        else:
            print(f"You outscored the computer {user_total} to {com_total}. You win!")

def main() -> None:
    played = False
    while True:
        user_input = input("Would you like to play blackjack (y/n): ").lower()
        if user_input == 'y':
            play_game()
            played = True
        elif user_input == 'n':
            if played:
                print("Thank you for playing!")
            break
        else:
            print("That is not a valid answer.")
    
    
if __name__ == "__main__":
    main()
