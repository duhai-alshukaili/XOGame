import random
import copy

def intialize_board(size=3):
    """
    Intialize a game board given a size.

    Args:
        size (int): The dimension of the 2D game board

    Returns:
        An empty game board  as a `size X size` 2D array
    """
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

def display_board(board):
    """
    Display the game board.

    Args:
        board (2d array): The game board to be displayed.
    
    Returns:
        None
    """

    # add horizontal line at the top
    [print("|---|", end="") if c == 0 
        else print("---|", end="") 
        for c in range(len(board))]
    print()

    for i,row in enumerate(board):

        # print cell contents
        [print("|{:^3s}|".format(cell), end="") if c == 0 
         else print("{:^3s}|".format(cell), end="") 
         for c, cell in enumerate(row)]
    
           
        print() # end of line for cell contents line

        # add horizontal lines between rows
        [print("|---|", end="") if c == 0 
         else print("---|", end="") 
         for c in range(len(row))]
        
        print() # end of line for hoirzontal cell

    print()


def get_user_move(board):
    """
    Get the row and col values from the use based on the current board

    Args:
        board (2D array): The game board to be displayed.
    
    Returns:
        None
    """
    while True:
        try:
            row = int(input("Enter the row   (1 to {}): ".format(len(board))))
            col = int(input("Enter the colum (1 to {}): ".format(len(board))))

            if 0 < row <= len(board) and 0 < col <= len(board) and \
                board[row-1][col-1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid input. Please choose an empty cell " 
                      + "within the board's boundries.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def make_move(board, row, col, player_symbol):
    """
    Update the game board with the player's move at the specified position.

    Args:
        board (2D array): The current game board.
        row (int): The row where the player wants to make a move.
        col (int): The column where the player wants to make a move.
        player_symbol (str): The symbol of the player making the 
            move ('X' or 'O').

    Returns:
        None
    """
    board[row][col] = player_symbol

def check_win(board, player_symbol):

    """
    Check for horizontal, vertical, and diagonal wins.

    Args:
        board (2D array): The current game board.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        True if the player of the given symbol complted a row, a column
        of a diaginal. False otherwise.
    """

    # Check the diagonals wins
    size = len(board)
    main_diag = [board[i][i] for i in range(size)]
    anti_diag = [board[i][size - 1 - i] for i in range(size)]

    if all(cell == player_symbol for cell in main_diag) \
        or all(cell == player_symbol for cell in anti_diag):
        return True
    
    # Check the horizontal wins
    for r in range(size):
        row = [board[r][c] for c in range(size)]

        if all(cell == player_symbol for cell in row):
            return True
    
    # Check the vertical wins
    for c in range(size):
        col = [board[r][c] for r in range(size)]

        if all(cell == player_symbol for cell in col):
            return True
    
    # could not find any wins
    return False

def check_draw(board):
    """
    Check if all cells on the board are filled and non has won

    Args:
        board (2D array): The current game board.
    Returns:
        True if it's a draw, otherwise, return False
    """
    return all(' ' not in row for row in board) \
        and not check_win(board, 'X') \
        and not check_win(board, 'O')

def get_random_computer_move(board):
    """
    Generate random row and column indices for the computer's 
    move on the given board.
    Args:
        board (2D array): The current game board.
    Returns:
        Tuple[int, int]: A tuple containing the random row and column indices 
        for the computer's move.
    """
    size = len(board)

    # Generate random indices until an empty cell is found
    r, c = random.randint(0, size - 1), random.randint(0, size - 1)
    while board[r][c] != ' ':
        r, c = random.randint(0, size - 1), random.randint(0, size - 1)
    
    return r, c

# -------------------------------------------------------------------------------
# The following functions are the constituent elements of a game.
# Using these functions, we can build an agent that "thinks" about
# possible moves using an algorithms such as Minimax search
# --------------------------------------------------------------------------------
def player(state):
    """Determine the current player based on the state of the game board.

    `player` function checks the number of 'X's and 'O's on the given game
    board to determine whose turn it is.

    Args:
        state (2D array): The current game board.

    Returns:
        str: The symbol ('X' or 'O') of the player whose turn it is based on
        the number of 'X's and 'O's on the board.
    """
    size = len(state)

    # Count the number of 'X' and 'O' symbols on the board
    xs = sum([state[r][c] == 'X' for r in range(size) for c in range(size)])
    os = sum([state[r][c] == 'O' for r in range(size) for c in range(size)])

    # Determine the player based on the count
    if xs == os:
        return 'X'
    else:
        return 'O'

def actions(state, player):
    """Generate a list of valid moves for the given player on the current game board.

    The `actions` function scans the provided game board and identifies all the
    empty cells where a player can make a valid move.
    Args:
        state (2D array): The current game board.
        player (str): The symbol ('X' or 'O') of the player for whom valid moves
                      are being generated.
    Returns:
        List[tuple]: A list of tuples representing the valid moves available to
                     the specified player. Each tuple contains the row and column
                     indices (starting from 1) of an empty cell on the board.
    """
    size = len(state)

    # Generate a list of valid moves as tuples (row, column)
    moves = [(r, c) for r in range(size) for c in range(size) if state[r][c] == ' ']

    return moves

def result(state, action):
    """Generate the resulting state after applying the specified action.

    The `result` function creates a deep copy of the current game state, determines
    the current player's symbol, and updates the copied state by making a move in
    the specified row and column according to the player's symbol.

    Args:
        state (2D array): The current game board.
        action (tuple): A tuple containing the row and column indices (starting from 1)
                        where the player wants to make a move.

    Returns:
        2D array: The new game board after applying the specified action.
    """
    r, c = action[0], action[1]

    state = copy.deepcopy(state)
    move = player(state)

    state[r][c] = move

    return state
    


def terminal(state):
    """Check if the current state of the tic-tac-toe game is terminal.

    The `terminal` function determines if the game has reached a terminal state,
    i.e., if either player 'X' or 'O' has won, or if the game has ended in a draw.

    Args:
        state (2D array): The current game board.

    Returns:
        bool: True if the game is in a terminal state (win or draw), False otherwise.
    """
    return check_win(state, 'X') \
        or check_win(state, 'O') \
        or check_draw(state)



    
def utility(state, max_player):
    """Calculate the utility value for the given state and maximizing player.

    The utility function assigns a score based on the outcome of the game for the
    specified player. It returns +100 if the maximizing player wins, -100 if the
    minimizing player wins, and 0 if the game is a draw.

    Args:
        state (2D array): The current game board.
        max_player (str): The symbol of the maximizing player.

    Returns:
        int: The utility value for the specified player.
    """

    
    if check_win(state, max_player):
        return 1000
    elif check_win(state, 'X' if max_player == 'O' else 'O'):
        return -1000
    elif check_draw(state):
        return 0
    else:
        return None


def is_cutoff(depth):
    """Check if the search should be cut off at the specified depth.

    The `is_cutoff` function determines whether the search should be terminated
    based on the given depth. It is commonly used in algorithms like Minimax with
    alpha-beta pruning to limit the depth of the search.

    Args:
        depth (int): The current depth of the search.

    Returns:
        bool: True if the search should be cut off at the specified depth, False otherwise.
    """
    return depth == 4


def alpha_beta_search(state):
    """Get the optimal move for the computer player using the Minimax algorithm with alpha-beta search.

    The `get_computer_move` function determines the best move for the computer player
    by applying the Minimax algorithm. It evaluates the possible moves based on the current
    game state, and returns the value and corresponding move that maximizes the utility
    for the computer player.

    Args:
        state (2D array): The current game board.

    Returns:
        tuple: A tuple containing the utility value of the best move and the corresponding
               move itself. The move is represented as a tuple containing the row and
               column indices (starting from 1) on the board.
    """
    max_player = player(state)
    value, move = max_value(state, max_player, 0 , float('-inf'), float('inf'))
    return value, move


def max_value(state, max_player, depth, alpha, beta):
    """Evaluate the maximum value for the current state in the Minimax algorithm.

    The `max_value` function represents the maximizing player's perspective in the
    Minimax algorithm. It recursively explores the game tree to find the move that
    maximizes the utility value for the maximizing player.

    Args:
        state (2D array): The current game board.
        max_player (str): The symbol ('X' or 'O') of the maximizing player.
        alpha (float): The alpha value for alpha-beta pruning.
        beta (float): The beta value for alpha-beta pruning.

    Returns:
        tuple: A tuple containing the maximum utility value and the corresponding move.
               The move is represented as a tuple containing the row and column indices
               (starting from 1) on the board.
    """
    p = player(state)  # Get the current player

    # Check if the current state is terminal
    if terminal(state):
        # If terminal, return the utility value and no specific move
        return utility(state, max_player), None

    # Check if the search should be cut off at the specified depth
    if is_cutoff(depth):
        # If cut off, return the evaluated board score and no specific move
        return evaluate_board(state, max_player), None

    v = float('-inf')
    move = None

    for a in actions(state, p):

        # Recursively call the min_value function to explore the opponent's moves
        # and obtain the minimum utility value and corresponding move
        v2, a2 = min_value(result(state, a), max_player, depth+1, alpha, beta)


        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)

        if v >= beta:
            return v, move  # Prune

    return v, move


def min_value(state, max_player, depth, alpha, beta):
    """Evaluate the minimum value for the current state in the Minimax algorithm.

    The `min_value` function represents the minimizing player's perspective in the
    Minimax algorithm. It recursively explores the game tree to find the move that
    minimizes the utility value for the minimizing player.

    Args:
        state (2D array): The current game board.
        max_player (str): The symbol ('X' or 'O') of the maximizing player.
        alpha (float): The alpha value for alpha-beta pruning.
        beta (float): The beta value for alpha-beta pruning.

    Returns:
        tuple: A tuple containing the minimum utility value and the corresponding move.
               The move is represented as a tuple containing the row and column indices
               (starting from 1) on the board.
    """
    p = player(state)  # Get the current player

    # Check if the current state is terminal
    if terminal(state):
        # If terminal, return the utility value and no specific move
        return utility(state, max_player), None
    
    # Check if the search should be cut off at the specified depth
    if is_cutoff(depth):
        # If cut off, return the evaluated board score and no specific move
        return evaluate_board(state, max_player), None

    v = float('inf')
    move = None

    for a in actions(state, p):

        # Recursively call the max_value function to explore the computer player's moves
        # and obtain the maximum utility value and corresponding move
        v2, a2 = max_value(result(state, a), max_player, depth + 1, alpha, beta)


        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)

        if v <= alpha:
            return v, move  # Prune

    return v, move


def evaluate_board(board, player):
    """
    Evaluate the Tic-Tac-Toe board based on the specified heuristic.

    Args:
        board (2D array): The current game board.
        player (str): The symbol of the player ('X' or 'O') for whom the evaluation is done.

    Returns:
        int: The heuristic score for the current board position.
    """
    opponent = 'X' if player == 'O' else 'O'
    score = 0

    # Check for 3-in-a-line, 2-in-a-line, and 1-in-a-line for the specified player
    for line in get_all_lines(board):
        count_player = line.count(player)
        count_opponent = line.count(opponent)
        count_empty = line.count(' ')

        if count_opponent == 0:
            # Computer's seeds only
            if count_player == 3:
                score += 30
            elif count_player == 2 and count_empty == 1:
                score += 10
            elif count_player == 1 and count_empty == 2:
                score += 1
        elif count_player == 0:
            # Opponent's seeds only
            if count_opponent == 3:
                score -= 30
            elif count_opponent == 2 and count_empty == 1:
                score -= 10
            elif count_opponent == 1 and count_empty == 2:
                score -= 1

    return score


def get_all_lines(board):
    """
    Generate all possible lines (rows, columns, and diagonals) from the Tic-Tac-Toe board.

    Args:
        board (2D array): The current game board.

    Returns:
        List[List[str]]: A list containing all possible lines in the board.
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    lines.extend(zip(*board))

    # Diagonals
    lines.append([board[i][i] for i in range(len(board))])
    lines.append([board[i][len(board) - 1 - i] for i in range(len(board))])

    return lines



def human_vs_computer_game_loop():
    """Run the Human vs Computer loop for a tic-tac-toe game.

    This function initializes the game board, allows the user to choose their symbol
    ('X' or 'O'), and alternates between the human player and the computer player until
    the game is won or drawn. The game state is displayed after each move, and the winner
    or a draw is announced at the end.

    The game loop continues until the user decides to exit.

    Returns:
        None
    """
    board_size = int(input("Enter the size of the board (3 to 9): "))
    board = intialize_board(board_size)

    human_symbol = input("Choose you symbol (X or O): ").upper()
    computer_symbol = 'X' if human_symbol == 'O' else 'O'

    current_player = 'X'

    count = 0

    while True:
        # print(f"Available Moves for {player(board)}: {actions(board, player(board))}")
        display_board(board)

        if current_player == human_symbol:
            row, col = get_user_move(board)
        else:

            # Make some random moves to avoid evaluating an empty board at the start of the game.
            # This is a temporary solution; ideally, replace this with an open game database.
            if count < (board_size - 2) * 2:    
                row, col = get_random_computer_move(board)
            else:
                value, (row, col) = alpha_beta_search(board)
            print(f"Computer played in cell ({row + 1}, {col + 1})")

        make_move(board, row, col, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It is a draw!")
            break

        count += 1

        current_player = 'O' if current_player =='X' else 'X'

def human_vs_human_game_loop():
    """
    Run a game loop for a Tic-Tac-Toe game where two human players compete against each other.

    This function initializes the game board based on user input for size (between 3x3 to 9x9),
    lets each player choose their symbol ('X' or 'O'), and alternates turns between the two
    players. The game continues until one player wins by aligning their symbols vertically,
    horizontally, or diagonally without any breaks, or until the game board is full and the game
    is declared a draw. The name of each player is requested for personalized messaging during
    gameplay.

    Args:
        None

    Returns:
        None
    """
    
    board_size = int(input("Enter the size of the board (3 to 9): "))
    board = intialize_board(board_size)

    human_symbol1 = input("Choose you symbol for the first player (X or O): ").upper()
    # human_symbol2 = 'X' if human_symbol1 == 'O' else 'O'

    human_name1 = input("Enter the name of the first player: ")
    human_name2 = input("Enter the name of the second player: ")

    current_player = 'X'


    count = 0

    while True:
        display_board(board)

        # get a move
        row, col = get_user_move(board)

        if current_player == human_symbol1:
            print(f"{human_name1} played in cell ({row+1}, {col+1})")
        else:
            print(f"{human_name2} played in cell ({row+1}, {col+1})")

        make_move(board, row, col, current_player)

        if check_win(board, current_player):
            display_board(board)

            if current_player == human_symbol1:
                print(f"{human_name1} wins!")
            else:
                print(f"{human_name2} wins!")
            break

        elif check_draw(board):
            display_board(board)
            print("It is a draw!")
            break

        count += 1

        current_player = 'O' if current_player =='X' else 'X'

def test_eval_board():

     # Boards where 'X' has the advantage
    board4_x_advantage = [
        ['X', 'O', ' ', 'X'],
        ['O', ' ', ' ', 'O'],
        [' ', ' ', 'X', 'O'],
        ['O', ' ', ' ', 'X']
    ]
    print(evaluate_board(board4_x_advantage, 'X'))

    board5_x_advantage = [
        ['X', 'O', ' ', 'X', ' '],
        ['O', 'X', ' ', 'O', 'O'],
        ['O', ' ', 'X', 'O', ' '],
        ['O', ' ', 'X', 'X', ' '],
        ['X', 'O', 'X', ' ', 'O']
    ]

    print(evaluate_board(board5_x_advantage, 'X'))

    board6_x_advantage = [
        ['X', 'O', ' ', 'X', ' ', 'O'],
        ['O', 'X', ' ', 'O', ' ', 'X'],
        [' ', ' ', 'X', 'O', ' ', 'O'],
        ['O', ' ', ' ', 'X', ' ', ' '],
        ['X', 'O', ' ', ' ', 'O', 'X'],
        [' ', 'X', 'O', 'O', 'X', ' ']
    ]
    print(evaluate_board(board6_x_advantage, 'O'))

    # Boards where 'O' has the advantage
    board4_o_advantage = [
        ['X', 'O', ' ', 'X'],
        ['O', 'O', ' ', 'O'],
        [' ', ' ', 'X', 'O'],
        ['O', ' ', ' ', 'X']
    ]
    print(evaluate_board(board4_o_advantage, 'X'))

    board5_o_advantage = [
        ['X', 'O', ' ', 'X', ' '],
        ['O', 'O', ' ', 'O', ' '],
        [' ', ' ', 'X', 'O', ' '],
        ['O', ' ', ' ', 'X', ' '],
        ['X', 'O', ' ', ' ', 'O']
    ]
    print(evaluate_board(board5_o_advantage, 'X'))

    board6_o_advantage = [
        ['X', 'O', ' ', 'X', ' ', 'O'],
        ['O', 'O', ' ', 'O', ' ', 'X'],
        [' ', ' ', 'X', 'O', ' ', 'O'],
        ['O', ' ', ' ', 'X', ' ', ' '],
        ['X', 'O', ' ', ' ', 'O', 'X'],
        [' ', 'X', 'O', 'O', 'X', ' ']
    ]
    print(evaluate_board(board6_o_advantage, 'X'))

if __name__ == '__main__':

    # human_vs_computer_game_loop()
    human_vs_human_game_loop()

   