class Square:
    def __init__(self, square_type, target=False):
        self.square_type = square_type  # Types: "empty", "fixed", "movable", "goal"
        self.is_target = target         # True if it's a goal position for colored squares

    def __str__(self):
        return self.square_type[0].upper()

class Board:
    def __init__(self, n):
        self.size = n
        self.grid = [[Square("empty") for _ in range(n)] for _ in range(n)]
        self.movable_positions = []  # Track movable squares for easy access

    def add_square(self, x, y, square_type, target=False):
        self.grid[x][y] = Square(square_type, target)
        if square_type == "movable":
            self.movable_positions.append((x, y))
    
    def display(self):
        for row in self.grid:
            print(" ".join(str(square) for square in row))
        print()

    def is_valid_move(self, x, y, direction):
        # Check boundary and fixed square constraints
        if direction == "up" and x > 0 and self.grid[x-1][y].square_type == "empty":
            return True
        elif direction == "down" and x < self.size - 1 and self.grid[x+1][y].square_type == "empty":
            return True
        elif direction == "left" and y > 0 and self.grid[x][y-1].square_type == "empty":
            return True
        elif direction == "right" and y < self.size - 1 and self.grid[x][y+1].square_type == "empty":
            return True
        return False

    def move_square(self, x, y, direction):
        # Move the square in the specified direction if valid
        if not self.is_valid_move(x, y, direction):
            return False

        # Example logic for moving a square (simplified)
        if direction == "up":
            self.grid[x-1][y], self.grid[x][y] = self.grid[x][y], Square("empty")
            x -= 1
        # Add other directions similarly
        # Update the movable_positions if needed
        return True

    def is_goal_state(self):
        # Check if all movable squares are on goal positions
        for x, y in self.movable_positions:
            if not self.grid[x][y].is_target:
                return False
        return True
class GameController:
    def __init__(self, board):
        self.board = board

    def play(self):
        self.board.display()
        while not self.board.is_goal_state():
            move = input("Enter move (e.g., 'move 0 1 up'): ")
            # Parse the input to get the x, y, and direction
            try:
                _, x, y, direction = move.split()
                x, y = int(x), int(y)
                if not self.board.move_square(x, y, direction):
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input format.")
            self.board.display()
        print("Congratulations! You solved the puzzle.")
def initialize_game():
    # Example: create a 5x5 board with fixed and goal positions
    board = Board(5)
    board.add_square(1, 1, "fixed")
    board.add_square(2, 2, "movable", target=True)
    # Add other squares as needed for the game setup
    return GameController(board)

# Start the game
game = initialize_game()
game.play()