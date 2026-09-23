A command-line Blackjack game built in Python as part of my 100 Days of Python learning journey.

The project focuses on practicing functions, loops, conditional logic, lists, return values, and coordinating multiple functions through a main() game loop.

Features
Deals random cards to the player and computer.
Supports standard card values from 2–10, face cards, and Aces.
Detects Blackjack when the initial hand contains two cards totaling 21.
Handles Aces by converting an Ace from 11 to 1 when the hand exceeds 21.
Allows the player to draw additional cards or stop.
The computer automatically draws until its score reaches at least 17.
Compares the final player and computer scores.
Detects busts and determines the winner.
How the Game Works
1. Initial Deal

The player and computer each receive two cards.

Player → 2 cards
Computer → 2 cards
2. Player Turn

The player can choose to:

D (Deal) — draw another card.
P (Pass) — stop drawing.

After drawing a card, the game recalculates the player's score.

3. Computer Turn

When the player passes, the computer takes its turn automatically.

The computer continues drawing while its score is below 17.

4. Score Calculation

The program handles several Blackjack rules:

An Ace initially has a value of 11.
If the hand exceeds 21 and contains an Ace, the Ace can be changed to 1.
A starting two-card score of 21 is treated as Blackjack.
5. Winner Evaluation

The program compares the final scores and determines whether:

The player wins.
The computer wins.
The game is a draw.
Either side has busted.
Either side has Blackjack.
Main Functions
deal_hand()

Randomly selects and returns a card value.

calculate_score(card)

Calculates the current hand's score and handles Blackjack and Ace conversion.

compare_score(user_score, comp_score)

Compares the player's and computer's final scores and returns the game result.

user_turn(user_cards)

Handles the player's decision to draw or stop.

computer_turn(comp_cards)

Handles the computer's automatic drawing behavior.

main()

Controls the overall game flow and coordinates the different functions.

What I Practiced

This project helped me practice:

Functions and function calls
Parameters and return values
while loops
for loops
Conditional statements
Lists and list mutation
Random number selection
Boolean conditions
Variable scope
State changes between functions
Tracing program execution
Debugging function interactions
Key Learning

One of the biggest lessons from this project was that understanding individual functions is different from understanding how the whole program flows.

For example:

main()
  ↓
user_turn()
  ↓
return decision
  ↓
main()
  ↓
continue or computer_turn()
  ↓
calculate_score()
  ↓
compare_score()

I also learned that changing a list inside a function can affect the original list because lists are mutable, while a calculated score needs to be explicitly recalculated after the hand changes.

Learning Goal

This project is part of my progression from understanding individual Python concepts toward being able to coordinate them into a complete program.

The main goal wasn't simply to make the game run, but to improve my ability to:

understand → trace → build → test → debug

without relying entirely on a finished solution.

Technologies
Python
Thonny
Python Standard Library (random)
Project Status

Completed — Core Blackjack game

Future improvements could include adding a replay option, improving the user interface, and refining the Blackjack rule handling.
