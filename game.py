import random
import inquirer

class Move:
    def __init__(self, name):
        self.name = name

class Rock(Move):
    def __init__(self):
        super().__init__("Rock")

class Paper(Move):
    def __init__(self):
        super().__init__("Paper")

class Scissors(Move):
    def __init__(self):
        super().__init__("Scissors")

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.move = None
        self.wins = 0
        self.losses = 0

    def choose_move(self, move):
        self.move = move

    def playerMove(self):
        while self.move is None:
            questions = [
                inquirer.List('choice',
                            message="Select your move...",
                            choices=['Rock', 'Paper', 'Scissors'],
                        ),
            ]
            answers = inquirer.prompt(questions)
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
        self.moves = [Rock(), Paper(), Scissors()]
        self.results = []
        self.player = player
        self.computer = computer

    def computer_move(self):
        self.computer.choose_move(random.choice(self.moves))

    def determine_winner(self):
        if self.player.move.name == self.computer.move.name:
            return "It's a tie!"
        elif (self.player.move.name == "Rock" and self.computer.move.name == "Scissors") or \
             (self.player.move.name == "Paper" and self.computer.move.name == "Rock") or \
             (self.player.move.name == "Scissors" and self.computer.move.name == "Paper"):
            return "You win! :D"
        else:
            return "Computer wins! :("

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")

        self.player.playerMove()
        self.computer_move()

        print(f"Player choice: {self.player.move.name}")
        print(f"Computer choice: {self.computer.move.name}")

        result = self.determine_winner()
        print(result)

        self.results.append(result)

        f = open("Game_Results.txt", "w")
        f.write(f"Player choice: {self.player.move.name}\n")
        f.write(f"Computer choice: {self.computer.move.name}\n")
        f.write(result)
        f.close()

player = Player()
computer = Player("Computer")
game = Game(player, computer)


game.play_game()