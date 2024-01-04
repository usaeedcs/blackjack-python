# Blackjack Game in Python

This repository contains a simple text-based version of the popular card game Blackjack. The game is implemented in Python and uses object-oriented programming principles.

## Design Choices

- **Card Class**: This class holds characteristics for the point value, name, and suit of each individual playing card. An `__add__` method was included to facilitate summing card values for upcoming card game implementations. 

- **Deck Class**: This class handles the 52 cards in the collection. It shuffles the deck, draws cards, puts them back in the deck, and resets the deck. The deck of cards is represented by a list data structure.

- **Hand Class**: This class, which can hold a variety of cards, represents the player's hand. It includes instructions on how to remove cards from the hand and figure out the hand's overall score.

## Changes and Improvements

- A dictionary (`card_values`) is used to map the names of the cards to their corresponding values (e.g., "Ace" maps to 11, "King" to 10). This makes the code more readable and allows easy retrieval of card values.

- The card names in the `names` list of the `Deck` class are reordered to follow the standard order.

- The `Deck` class was already well-structured in Project 2. The original logic was kept and some parts were rearranged to improve readability.

- The logic for calculating the score in the `Hand` class was revised in Project 3. It now correctly handles the value of Aces, where an Ace can have a value of 11 or 1 depending on the hand's total score.

## Data Structures Used

- **Classes**: The code utilizes three classes: `Card`, `Deck`, and `Hand`. This object-oriented approach helps in encapsulating data and behavior related to cards, the deck, and the player's hand.

- **Lists**: Lists are used to store the cards in the `Deck` and the player's `Hand`.

## Challenges Faced

- **Handling the Ace card**: The primary challenge was dealing with the value of Aces, which can be either 1 or 11. This was resolved by keeping track of the number of Aces in the hand and adjusting the total score accordingly to prevent busting.

- **String Representation**: Creating a readable and meaningful string representation of cards and hands was essential. The `__str__` method in the `Card` class helped in achieving this by providing a clear card representation.

- **User Input Validation**: Ensuring that the player's input for hitting or standing was valid required additional input validation checks in the gameplay loop.

## Future Improvements

- More attributes and methods could be added to the Card class to handle a more sophisticated card game.

- Support for multiple decks or unique deck configurations could be added to the Deck class to give it greater flexibility.

- A user interface could be designed to show cards and let players engage with the game graphically to make it more interactive.

## Conclusion

Overall, this solution offers a strong basis for a simple card game and exhibits the essential functionality needed for controlling a player's hand and deck of cards. It can be enhanced and altered to provide a variety of card games with special dynamics.
