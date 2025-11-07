import turtle as t
import random

screen = t.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

turt = t.Turtle()
turt.speed(0)
turt.color("white")
turt.hideturtle()

# --- Draw frame ---
def frame():
    turt.penup()
    turt.goto(-300, -300)
    turt.pendown()
    for _ in range(4):
        turt.forward(600)
        turt.left(90)

frame()

# --- Maze setup ---
GRID_SIZE = 6
CELL_SIZE = 100
maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def goto_cell(x, y):
    turt.penup()
    turt.goto(-300 + x * CELL_SIZE, -300 + y * CELL_SIZE)
    turt.pendown()

def draw_cell(x, y, color):
    turt.fillcolor(color)
    turt.begin_fill()
    goto_cell(x, y)
    for _ in range(4):
        turt.forward(CELL_SIZE)
        turt.left(90)
    turt.end_fill()

def carve(x, y):
    maze[y][x] = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[ny][nx] == 1:
            maze[ny][nx] = 0
            carve(nx, ny)

carve(0, 0)

# Draw maze
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        color = "black" if maze[y][x] == 0 else "white"
        draw_cell(x, y, color)

screen.exitonclick()

import random
import time
import os

GRID_SIZE = 11  # should be odd (cells + walls)
maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def print_maze():
    """Display the maze in the console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
    for row in maze:
        print(' '.join('⬜' if cell == 1 else '⬛' for cell in row))
    time.sleep(0.05)

def get_neighbors(x, y):
    """Get neighboring cells two steps away (so we keep walls between)."""
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < GRID_SIZE - 1 and 0 < ny < GRID_SIZE - 1:
            neighbors.append((nx, ny))
    return neighbors

def carve(x, y):
    """Recursive backtracking maze generation."""
    maze[y][x] = 0  # mark current cell as open
    print_maze()
    for nx, ny in get_neighbors(x, y):
        if maze[ny][nx] == 1:
            # Remove wall between current and next cell
            maze[y + (ny - y)//2][x + (nx - x)//2] = 0
            carve(nx, ny)

# --- Initialize maze ---
# Make borders walls and interior possible paths
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        maze[y][x] = 1

# Start carving from top-left inside the border
carve(1, 1)

# Mark start and end
maze[1][0] = 0  # entrance
maze[GRID_SIZE-2][GRID_SIZE-1] = 0  # exit

print_maze()
print("✅ Maze generation complete!")
