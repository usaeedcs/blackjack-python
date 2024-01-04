import random

class Deck:

    def __init__(self):
        """
        # Constructor to initialize the deck with 52 cards based on suits and names
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        names = ['Ace', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'Jack', 'Queen', 'King']

        # Using a dictionary to map card names to their corresponding values
        card_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                       '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

        self.cards = [Card(card_values[name], name, suit)
                      for suit in suits for name in names]
        self.shuffle()  # Shuffling the deck after it's created

    def shuffle(self):
        """
        This function is for shuffling deck
        Params:
            None
        Returns:
            None
        """
        random.shuffle(self.cards)

    def draw_card(self):
        # Drawing a single card from the deck
        return self.cards.pop()

    def __len__(self):
        # Returning the number of cards remaining in the deck
        return len(self.cards)


class Card:
    def __init__(self, value, name, suit):
        """
        Constructor to initialize a card with its value, name, and suit
        params:
            value: int
            name: str
            suit: str
        Returns:
            None
        """

        self.value = value
        self.name = name
        self.suit = suit

    def __str__(self):
        """
        String representation of the card
        Returns: None
        """
        return f"{self.name} of {self.suit}"

    def __add__(self, card2):
        """
        Helper method to add card instances together or a card and an integer
        Params:
            Card2: Card | int
        Returns:
            int
        """
        if isinstance(card2, Card):
            return self.value + card2.value
        elif isinstance(card2, int):
            return self.value + card2
        else:
            raise TypeError("Unsupported operand type for +")

    def __radd__(self, card2):
        """
        Helper method to perform reverse addition if the first operand does not support addition with the second operand
        Params:
            Card2: Card | int
        Returns:
            int
        """
        return self.__add__(card2)


class Hand:
    def __init__(self, size=5):
        """
        Constructor to initialize the hand with an empty list of cards
        Params:
            size: int
        Returns:
            None
        """
        self.cards = []
        self.size = size

    def discard(self, card):
        """
        Method to discard a card from the hand
        Params:
            Card: Card
        Returns:
            None
        """
        if card in self.cards:
            self.cards.remove(card)

    def calc_score(self):
        """
        This function is for calculating scoring optimally
        Params:
            None
        Returns:
            int
        """
        score = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.name == 'Ace')
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def __len__(self):
        """
        Returning the number of cards in the hand
        Returns:
            int
        """
        return len(self.cards)

    def add_card_to_hand(self, card):
        """
        Method to add a card to the hand
        Params:
            card: Card
        Returns:
            int
        """
        if len(self.cards) < self.size:
            self.cards.append(card)
        else:
            raise ValueError("Hand is already full. Cannot add more cards.")

    def print_hand(self):
        """
        This is helper function for printing hand
        Params:
            None
        Returns:
            None
        """
        for card in self.cards:
            print(card)
        print(f"Score: {self.calc_score()}\n")


# Implement gaming functionality
def play_blackjack():

    # Helper method to show hands at the end of the game
    def show_game_stats():
        print("\n----------Player's Hand-----------\n")
        player_hand.print_hand()
        print("\n----------Dealers's Hand-----------\n")
        dealer_hand.print_hand()

    # Writing main loop logic
    playersState = True
    while True:
        deck = Deck()
        player_hand = Hand()

        # Withdrawing cards
        player_hand.add_card_to_hand(deck.draw_card())
        player_hand.add_card_to_hand(deck.draw_card())

        dealer_hand = Hand()
        dealer_hand.add_card_to_hand(deck.draw_card())
        dealer_hand.add_card_to_hand(deck.draw_card())

        # writing players logic
        player_score = 0
        dealers_score = 0
        while True:
            print("\n--------Player's Hand--------\n")
            player_hand.print_hand()
            player_score = player_hand.calc_score()
            # Checking for blackjack or bust
            if player_score == 21:
                print("Blackjack! You win!")
                playersState = False
                break
            if player_score > 21:
                print("Player busted! You lose!")
                playersState = False
                break

            # Asking player for next move
            choice = input(
                "Do you want to hit or stand? (Enter 'hit' or 'stand'): ").lower()

            if choice == "hit":
                player_hand.add_card_to_hand(deck.draw_card())
            elif choice == "stand":
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        # if player is busted show game stats else dealers turn
        if not playersState:
            show_game_stats()
            break
        else:
            print("\n------Dealer's Hand------\n")
            dealer_hand.print_hand()
            dealers_score = dealer_hand.calc_score()
            while dealers_score < 17:
                dealer_hand.add_card_to_hand(deck.draw_card())
                dealers_score = dealer_hand.calc_score()

        print("\n------Dealer's Hand---------")
        dealer_hand.print_hand()

        if player_score == 21:
            print("Blackjack! You win!")
        elif player_score <= 21:
            # Proceed with comparing scores if the player did not bust
            if dealers_score > 21 or player_score > dealers_score:
                print("Congratulations! You win!")  # Player wins
            elif player_score == dealers_score:
                print("It's a tie!")
            else:
                print("Dealer wins! You lose!")
        else:
            print("Player busted! You lose!")

        show_game_stats()
        play_again = input(
            "Do you want to play again? (Enter 'yes' or 'no'): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    play_blackjack()
