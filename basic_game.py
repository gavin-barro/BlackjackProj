import card_list
import random

deck_of_cards = card_list.generate_cards()
card_count = 208  # 52 cards * 4 decks

class Card:
    def __init__(self, deck_of_cards: list[str]):
        # EX: King of Diamonds
        self.name = random.choice(deck_of_cards)
        # EX: King
        self.card = self.name.split(" ")[0]
        # EX: 10
        self.value = None
    
    def __str__(self):
        return f"Card: {self.name}" 

def card_math(cards: list[Card], total: int = 0, ace_count: int = 0) -> tuple[int, int]:
    for card in cards:
        if card.card in {'Jack', 'Queen', 'King'}:
            card.value = 10
        elif card.card == "Ace":
            card.value = 11
            ace_count += 1
        elif card.card.isdigit():  # Check if it's a number
            card.value = int(card.card)  # Convert "2" to 2, etc.
        total += card.value
    
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    
    return total, ace_count      

def play_game() -> None:
    global deck_of_cards
    global card_count
    
    user_card1 = Card(deck_of_cards)
    deck_of_cards.remove(user_card1.name)
    card_count -= 1
    user_card2 = Card(deck_of_cards)
    deck_of_cards.remove(user_card2.name)
    card_count -= 1
    
    user_total, user_ace = card_math([user_card1, user_card2])
    
    com_card1 = Card(deck_of_cards)
    deck_of_cards.remove(com_card1.name)
    card_count -= 1
    com_card2 = Card(deck_of_cards)
    deck_of_cards.remove(com_card2.name)
    card_count -= 1
    
    com_total, com_ace = card_math([com_card1, com_card2])
    
    user_msg = f"Your cards are: {user_card1.name} and {user_card2.name}. This adds up to {user_total}"
    print(user_msg)
    
    com_msg = f"Your opponent has a {com_card2.name}"
    print(com_msg)
    
    if user_total == 21:
        print("Blackjack! You win!!")
        print("Game Over!")
    elif com_total == 21:
        print("The com got Blackjack")
        print("Game Over!")
    else:
        while True:
            user_input = input("Would you like to hit? (y/n) ").lower()
            if user_input == 'n':
                break
            elif user_input == 'y':
                new_card = Card(deck_of_cards)
                card_count -= 1
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
                new_card = Card(deck_of_cards)
                card_count -= 1
                com_total, com_ace = card_math([new_card], com_total, com_ace)
                print(f"The computer drew a {new_card.name}. Computer total: {com_total}")
                if com_total > 21:
                    print("Computer busted! You win!")
                return
            if com_total == user_total:
                print(f"The computer and user both have {user_total}. Push!")
            elif com_total > user_total:
                print(f"The computer outscored you {com_total} to {user_total}. Computer wins!")
            else:
                print(f"You outscored the computer {user_total} to {com_total}. You win!")
    
    # Shuffle of deck if it is half empty
    if card_count < 104:
        deck_of_cards = card_list.generate_cards()
        card_count = 208

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
