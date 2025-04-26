import turtle
import random

MAP = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','B','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1','B','1'],
    ['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],
    ['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1',' ','1','1','1',' ','1','1','-','1','1',' ','1','1','1',' ','1','1'],
    [' ',' ',' ',' ',' ','1',' ','1','s','p','o','1',' ','1',' ',' ',' ',' ',' '],
    ['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],
    ['1',' ',' ',' ','1',' ',' ',' ',' ','P',' ',' ',' ',' ','1',' ',' ',' ','1'],
    ['1','B','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','B','1'],
    ['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],
    ['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

# Calculate map size and offsets to center the map
TILE_SIZE = 20
MAP_WIDTH = len(MAP[0]) * TILE_SIZE
MAP_HEIGHT = len(MAP) * TILE_SIZE

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Compute starting position to center the map
start_x = -MAP_WIDTH // 2
start_y = MAP_HEIGHT // 2 - TILE_SIZE  # Adjusted for turtle drawing from center

# Wall Setup
wall_block = turtle.Turtle()
wall_block.shape("square")
wall_block.color("blue")
wall_block.penup()
wall_block.speed(0)
wall_block.hideturtle()

walls = []

for y_index in range(len(MAP)):
    row = MAP[y_index]
    for x_index in range(len(row)):
        char = row[x_index]
        screen_x = start_x + (x_index * TILE_SIZE)
        screen_y = start_y - (y_index * TILE_SIZE)

        if char == '1':
            block = wall_block.clone()
            block.goto(screen_x, screen_y)
            block.showturtle()
            walls.append(block)

# Screen setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

def find_pacman_spawn():
    for y_index in range(len(MAP)):
        row = MAP[y_index]
        for x_index in range(len(row)):
            if row[x_index] == 'P':
                return x_index, y_index
    return None, None  # Return None if 'P' not found

def spawn_food():
    food_list = []
    for y_index in range(len(MAP)):
        row = MAP[y_index]
        for x_index in range(len(row)):
            if row[x_index] == ' ':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                food = turtle.Turtle()
                food.shape("circle")
                food.color("white")
                food.penup()
                food.goto(screen_x, screen_y)
                food.shapesize(0.5, 0.5)
                food_list.append(food)
    return food_list

def spawn_bonus():
    bonus_list = []
    for y_index in range(len(MAP)):
        row = MAP[y_index]
        for x_index in range(len(row)):
            if row[x_index] == 'B':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                bonus = turtle.Turtle()
                bonus.shape("circle")
                bonus.color("purple")
                bonus.penup()
                bonus.goto(screen_x, screen_y)
                bonus.shapesize(0.5, 0.5)
                bonus_list.append(bonus)
    return bonus_list

def spawn_ghost():
    ghost_list = []
    for y_index in range(len(MAP)):
        row = MAP[y_index]
        for x_index in range(len(row)):
            if row[x_index] == 's':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                sGhost = turtle.Turtle()
                sGhost.color("lightblue")
                sGhost.penup()
                sGhost.goto(screen_x, screen_y)
                sGhost.shapesize(1, 1, 0.5)
                ghost_list.append(sGhost)
            if row[x_index] == 'p':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                pGhost = turtle.Turtle()
                pGhost.color("pink")
                pGhost.penup()
                pGhost.goto(screen_x, screen_y)
                pGhost.shapesize(1, 1, 0.5)
                ghost_list.append(pGhost)
            if row[x_index] == 'o':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                oGhost = turtle.Turtle()
                oGhost.color("orange")
                oGhost.penup()
                oGhost.goto(screen_x, screen_y)
                oGhost.shapesize(1, 1, 0.5)
                ghost_list.append(oGhost)
            if row[x_index] == 'r':
                screen_x = start_x + (x_index * 20)
                screen_y = start_y - (y_index * 20)
                rGhost = turtle.Turtle()
                rGhost.color("red")
                rGhost.penup()
                rGhost.goto(screen_x, screen_y)
                rGhost.shapesize(1, 1, 0.5)
                ghost_list.append(rGhost)
    return ghost_list

# Pacman set  up
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.direction = "stop"

pacman_x, pacman_y = find_pacman_spawn()
if pacman_x is not None and pacman_y is not None:
    pacman.goto(start_x + (pacman_x * 20), start_y - (pacman_y * 20))

# Food setup
food_list = spawn_food()

# Bonus Setup
bonus_list = spawn_bonus()

# Ghost Setup
ghost_list = spawn_ghost()

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 280)
score_display.write("Score: 0", align="left", font=("Arial", 16, "normal"))


# Movement functions
def move_up():
    pacman.direction = "up"

def move_down():
    pacman.direction = "down"

def move_left():
    pacman.direction = "left"

def move_right():
    pacman.direction = "right"

def will_collide(new_x, new_y):
    for wall in walls:
        if wall.distance(new_x, new_y) < 20:
            return True
    return False

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


# Main game loop
def game_loop():
    new_x, new_y = pacman.xcor(), pacman.ycor()

    if pacman.direction == "up":
        new_y += 20
    elif pacman.direction == "down":
        new_y -= 20
    elif pacman.direction == "left":
        new_x -= 20
    elif pacman.direction == "right":
        new_x += 20

    if not will_collide(new_x, new_y):
        pacman.goto(new_x, new_y)

    # Border check
    if pacman.xcor() > 190:
        pacman.goto(-190, 10)
        pacman.direction = "right"
    
    if pacman.xcor() < -190:
        pacman.goto(190, 10)
        pacman.direction = "left"

    # Collision check
    for food in food_list:
        if pacman.distance(food) < 20:
            food.goto(1000, 1000)  # Move food off-screen
            food_list.remove(food)  # Remove from the list
            global score
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))
    
    for bonus in bonus_list:
        if pacman.distance(bonus) < 20:
            bonus.goto(1000, 1000)  # Move food off-screen
            bonus_list.remove(bonus)  # Remove from the list
            score += 50
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

    screen.update()
    turtle.ontimer(game_loop, 100)


game_loop()
turtle.done()