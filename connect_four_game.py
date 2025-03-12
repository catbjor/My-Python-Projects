from turtle import *
from freegames import line

# Dictionary to switch turns between players
turns = {'purple': 'pink', 'pink': 'purple'}

# Game state: Tracks the current player and stores the game board (8x8 grid)
state = {'player': 'purple', 'grid': [[''] * 8 for _ in range(8)]}

def grid():
    """Draw the Connect Four grid."""
    bgcolor('grey')
    
    # Draw vertical lines
    for x in range(-150, 200, 50):
        line(x, -200, x, 200)
    
    # Draw horizontal lines
    for y in range(-150, 200, 50):
        line(-200, y, 200, y)

    # Draw empty circles (game slots)
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')
    
    update()

def check_winner():
    """Check if a player has won the game."""
    grid = state['grid']
    
    # Check horizontal win
    for row in grid:
        for col in range(5):
            if row[col] and row[col] == row[col+1] == row[col+2] == row[col+3]:
                return row[col]  # Return the winning color

    # Check vertical win
    for col in range(8):
        for row in range(5):
            if grid[row][col] and grid[row][col] == grid[row+1][col] == grid[row+2][col] == grid[row+3][col]:
                return grid[row][col]

    # Check diagonal (\ direction) win
    for row in range(5):
        for col in range(5):
            if grid[row][col] and grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2] == grid[row+3][col+3]:
                return grid[row][col]

    # Check diagonal (/ direction) win
    for row in range(5):
        for col in range(3, 8):
            if grid[row][col] and grid[row][col] == grid[row+1][col-1] == grid[row+2][col-2] == grid[row+3][col-3]:
                return grid[row][col]

    return None  # No winner yet

def rap(x, y):
    """Handle player moves, draw circles, and check for a winner."""
    player = state['player']
    grid = state['grid']
    
    # Determine which column was clicked
    col = int((x + 200) // 50)

    if 0 <= col < 8:
        # Find the first empty row in the column (starting from the bottom)
        for row in range(7, -1, -1):
            if not grid[row][col]:
                grid[row][col] = player
                
                # Calculate the position to draw the piece
                x_pos = col * 50 - 200 + 25
                y_pos = row * 50 - 200 + 25
                
                up()
                goto(x_pos, y_pos)
                dot(40, player)
                update()

                # Check for a winner
                winner = check_winner()
                if winner:
                    print(f"{winner} wins! 🎉")
                    return
                
                # Switch turn to the next player
                state['player'] = turns[player]
                break

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(rap, 1)
done()

