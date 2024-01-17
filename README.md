# Rock, Paper, Scissors - Python Game

This is a Python game developed by me for my Certificate IV in Information Technology. This Python script runs a simple game of Rock, Paper, Scissors. The game is played between a human player and the computer.

The Game class is the main class that controls the game flow. It has the following methods:

`__init__(self, player, computer)`: This method initializes a new game with a human player and a computer player.

`computer_move(self)`: This method randomly selects a move for the computer player from the list of possible moves (Rock, Paper, or Scissors).

`determine_winner(self)`: This method determines the winner of the game based on the rules of Rock, Paper, Scissors. If both players choose the same move, it's a tie. Otherwise, Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.

`play_game(self)`: This method runs the game. It first welcomes the player, then prompts the human player to choose a move and randomly selects a move for the computer player. It then prints the choices of both players, determines the winner, and prints the result. The result is also appended to a list of results and written to a file named "Game_Results.txt".

The Player class represents a player in the game. It has a playerMove method that prompts the human player to choose a move, and a choose_move method that sets the move for the computer player.

The game is started by creating instances of the Player and Game classes and calling the play_game method on the Game instance.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/JordanRobo/Rock-Paper-Scissors.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Rock-Paper-Scissors
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the game, execute the following command:
    ```
    python3 game.py
    ```

