import random
import inquirer

# Class to represent a move
class Move: 
    def __init__(self, name):
        self.name = name

# Class to represent the Rock move
class Rock(Move): 
    def __init__(self):
        super().__init__("Rock")

# Class to represent the Paper move
class Paper(Move): 
    def __init__(self):
        super().__init__("Paper")

# Class to represent the Scissors move
class Scissors(Move): 
    def __init__(self):
        super().__init__("Scissors")

class Player: 
    def __init__(self, name="Player"):
        self.name = name # Player's name
        self.move = None # Player's move
        self.wins = 0 # Player's wins
        self.losses = 0 # Player's losses
        self.moves_history = []  # List to keep track of the player's move history
        self.scores = []  # List to keep track of the player's scores

    # Add the move to the move history list
    def choose_move(self, move):
        self.move = move
        self.moves_history.append(move)  

    # Add the score to the scores list
    def add_score(self, score):
        self.scores.append(score)  

    # Class method to create a computer player
    @classmethod 
    def create_computer_player(cls):
        return cls(name="Computer")

    # Method to get the player's move
    def playerMove(self): 
        while self.move is None:
            questions = [
                inquirer.List('choice',
                            message="Select your move...",
                            choices=['Rock', 'Paper', 'Scissors'],
                        ),
            ]
            answers = inquirer.prompt(questions)
            # Get the player's choice
            choice = answers['choice'] 
            if choice == 'Rock':
                self.move = Rock()
            elif choice == 'Paper':
                self.move = Paper()
            elif choice == 'Scissors':
                self.move = Scissors()
            else:
                print("Invalid choice. Please try again.")

class Game:
    def __init__(self, player, computer):
        self.moves = [Rock(), Paper(), Scissors()] # List of moves
        self.results = [] # List to keep track of the results
        self.player = player # Player
        self.computer = computer # Computer

    # Method to get the computer's move
    def computer_move(self): 
        self.computer.choose_move(random.choice(self.moves))

    # Method to determine the winner
    def determine_winner(self): 
        if self.player.move.name == self.computer.move.name:
            return "It's a tie!"
        elif (self.player.move.name == "Rock" and self.computer.move.name == "Scissors") or \
             (self.player.move.name == "Paper" and self.computer.move.name == "Rock") or \
             (self.player.move.name == "Scissors" and self.computer.move.name == "Paper"):
            return "You win! :D"
        else:
            return "Computer wins! :("
        
    # Method to ask the player if they want to play again
    def play_again(self): 
        questions = [
            inquirer.Confirm('play_again',
                             message="Do you want to play again?",
                             default=False),
        ]
        answer = inquirer.prompt(questions)['play_again']

        if answer:
            self.player.move = None
            self.computer.move = None
            self.play_game()
        else:
            print("Thank you for playing!")
            exit()
            
    # Method to play the game
    def play_game(self): 
        print("Welcome to Rock, Paper, Scissors!")

        self.player.playerMove()
        self.computer_move()

        print(f"Player choice: {self.player.move.name}")
        print(f"Computer choice: {self.computer.move.name}")

        result = self.determine_winner()
        print(result)

        self.results.append(result)

        with open("Game_Results.txt", "a") as f:
            f.write(f"\nPlayer choice: {self.player.move.name}\n")
            f.write(f"Computer choice: {self.computer.move.name}\n")
            f.write(result + "\n")

        self.play_again()


player = Player()
computer = Player("Computer")
game = Game(player, computer)


game.play_game()