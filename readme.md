# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The code follows the principles of the Minimax algorithm for the computer player, providing a challenging opponent for the human player.

## Design Choices

1. **Modular Structure:** The code is organized into functions, each responsible for a specific aspect of the game, such as initializing the board, displaying it, obtaining moves, and checking for a win or draw.

2. **User Interface:** The game provides a clear and user-friendly interface for the player, displaying the game board after each move and announcing the winner or a draw at the end of the game.

3. **Player Symbol Choice:** The player can choose their symbol ('X' or 'O') at the beginning of the game. The computer player takes the other symbol.

4. **Random Computer Moves:** Initially, the computer makes random moves until the Minimax algorithm is implemented. This adds an element of unpredictability before the computer starts playing optimally.

5. **Minimax Algorithm:** The Minimax algorithm is used to make optimal moves for the computer player. It explores the game tree, evaluating each possible move to find the one that leads to the best outcome.

6. **Alpha-Beta Pruning:** The Minimax algorithm is enhanced with alpha-beta pruning to improve its efficiency by pruning branches that cannot possibly influence the final decision.

## Concepts from CSDS3203 Introduction to AI

1. **Minimax Algorithm:** The implementation of the Minimax algorithm demonstrates the concept of adversarial search in game playing.

2. **Alpha-Beta Pruning:** The use of alpha-beta pruning optimizes the search space in the Minimax algorithm, showcasing an efficient way to explore the game tree.

3. **Utility Function:** The utility function assigns scores to different game states, helping the computer player make decisions based on the desirability of outcomes.

4. **Modular Design:** The modular design of the code aligns with the principles of abstraction and encapsulation, promoting code organization and readability.

5. **User Interaction:** The code incorporates user input for selecting the player's symbol and making moves, engaging the player in the gaming experience.

## How to Play

1. Run the code.
2. Enter the size of the board (3 to 9) when prompted.
3. Choose your symbol ('X' or 'O').
4. Follow the instructions to make moves.
5. Enjoy the game and try to beat the computer player!

Feel free to explore and modify the code to experiment with different strategies or improve the user interface. Have fun playing Tic-Tac-Toe!