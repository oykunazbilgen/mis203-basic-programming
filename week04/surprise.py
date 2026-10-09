import turtle
import random

# --- SCREEN AND ARTIST SETUP ---
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.title("Surprise Me - Generative Art")
screen.tracer(0)  # Turn off animation for instant drawing

artist = turtle.Turtle()
artist.hideturtle()  # Hide the turtle icon

# Color palette
colors = ["red", "cyan", "yellow", "lime", "magenta", "orange", "deep sky blue", "white"]

print("Generating artwork...")

# --- RANDOM PARAMETERS AND IF-ELSE SELECTIONS ---
# 1. Shape type selection (1: Hexagonal Spiral, 2: Star Pattern, 3: Rotating Squares)
shape_type = random.randint(1, 3)

# 2. Pen thickness selection (if-else condition)
is_thick = random.choice([True, False])
if is_thick:
    artist.width(3)
else:
    artist.width(1)

# 3. Number of steps (limited for shape 2 since it grows faster)
if shape_type == 2:
    steps = random.randint(50, 80)
else:
    steps = random.randint(70, 120)

# --- DRAWING LOOP (FOR LOOP & IF-ELSE) ---
for i in range(steps):
    # Pick a random color for each segment
    artist.pencolor(random.choice(colors))

    # Draw according to the chosen shape type
    if shape_type == 1:
        artist.forward(i * 3)
        artist.left(59)
    elif shape_type == 2:
        artist.forward(i * 4)
        artist.right(144)
    else:
        artist.forward(i * 2)
        artist.left(91)

screen.update()  # Show the whole drawing at once

# --- TERMINAL NOTIFICATION MESSAGE ---
names = {1: "Hexagonal Spiral", 2: "Hypnotic Star", 3: "Rotating Squares"}
print(f"Surprise! '{names[shape_type]}' was drawn in this run.")

# Close the window when clicked
screen.exitonclick()