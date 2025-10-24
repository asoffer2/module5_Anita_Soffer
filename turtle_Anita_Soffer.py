
# Turtle Village — Lite (Student Scaffold)
# Focus: loops, decisions, try/except, and small functions.
# Run this file locally (IDLE/Thonny/PyCharm).

"""
Pseudocode:
1. Import turtle and random
2. Set constants - canvas, dimensions, margins, size and theme list.
3. define turtle helpers:
   a. move_to (move from one coordinate to another)
   b. draw_line (from one coordinate to another)
   c. fill_rect_center (with color, begins and ends in top left corner)
   d. fill_triangle (fill a triangle with color given 3 coordinates)
   e. fill_circle_center (with color, fills from bottom)
4. define ask_choice_int:
   a. make an allowed set excluding duplicates
   b. print prompt and the allowed set
   c. collect user input while validating (with try / accept)-
      a while loop which returns input if correct and continues loop if not
5. define ask_choice_str:
   a. make allowed_lower- lowercase all allowed strings
   b. print prompt and allowed values
   c. collect user input lowercased (use same logic as 4)
6 define draw_roads-
   a. set pencolor and pensize
   b. create loops for rows and columns: for each row
       start at left edge and move right until the other edge. change
       starting point y value, x value stays constant. For each column
       start at the top margin and move down to bottom margin. Change x value
       in the starting point each time while y value stays at the top margin.
7. define draw_house_centered: draw a single house centered in the cell with colors.
   a. set width and height based on size and colors based on theme.
   b. decision structure: if the size is small, move to the top left corner of the
      rectangle, use a loop to draw a small rectangle. Nest if and use fill_rect_center
      with color based on theme. Make a possibility for medium and large,
      applying the same logic.
   c. decision structure for roof style: if it's a triangle,
      turn and draw_line from current point to apex.
      Turn and draw line from there to top left of the body rectangle. Create a decision
      structure for fill_triangle- colors based on theme.
   d. Move to a ratio if the width of the bottom of the rectangle to draw the door
      starting off to the side but centered around x = cx. Use a loop to draw a rectangle,
      width and height being a ratio of the body rectangle's width and height.
      fill_rect_center based on theme colors.
8. define draw_tree_near- drawing a small tree randomly to the left or right side of the house.
   a. set trunk (rectangle) width and height as a ratio of the body width and height.
   b. set the side as a random choice.
   c. set the center of the trunk (tx, ty) and draw a rectangle using (tw, th)- trunk height and
      width.
   d. fill_rect_center with brown
9. define draw_village to orchestrate:
   a. set cell width and height
   b. call draw_roads
   c. make a nested loop over rows and columns to compute the center
    coordinates of a cell - formulas given
   d. call draw_house_centered and draw_tree_near (pass in all arguments)
10. define main-
   a. print welcome message
   b. get validated user input for columns and rows separately using ask_choice_int
   c. get validated user input for size_key, theme_key, and roof_style using
      ask_choice_str
   d. set up window - canvas, speed, and tracer as false.
   e. call draw_village (pass in arguments).
   f. finalize with tracer, hide turtle and finish.
"""

import turtle as T
import random

# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40

SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}

# ---------- tiny turtle helpers (provided) ----------
def move_to(x, y):
    """Move turtle from x to y."""
    T.penup(); T.goto(x, y); T.pendown()


def draw_line(x1, y1, x2, y2):
    """Draw a line from x to y."""
    move_to(x1, y1); T.goto(x2, y2)


def fill_rect_center(cx, cy, w, h, color):
    """Fill a rectangle with color."""
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w / 2, cy + h / 2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()


def fill_triangle(p1, p2, p3, color): # each is a tuple
    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()


def fill_circle_center(cx, cy, r, color):
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()


# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
    """ Prompt the user for an integer within the allowed set;
        if an invalid input is given, display an error message and reprompt.
        Use a while loop to repeatedly request a valid number from the allowed
         list until a correct input is entered.
    """

    # a set is a list which only allows one unique item to exist, not any duplicates
    # if duplicates are given, set removes all duplicates
    allowed_set = set(allowed)
    prompt = prompt + str(allowed)

    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Invalid entry. Please enter an integer in the set.")
            continue
        if user_input not in allowed_set:
            print("Invalid entry. Please enter an integer in the set.")
            continue
        else:
            return user_input


def ask_choice_str(prompt, allowed):
    """Ask for a string in the allowed list (case-insensitive); reprompt on error.
    in a while loop, ask for a valid string from allowed list, exception is printed
    if incorrect number given, while loop continues until true.
    """
    allowed_lower = [a.lower() for a in allowed] # to match the user's lowercased input
    prompt = prompt + str(allowed_lower)

    while True:
        try:
            user_input = input(prompt).lower()
        except ValueError:
            print("Invalid entry. Please enter a valid word or letter")
            continue
        if user_input not in allowed_lower:
            print("Invalid entry. Please enter a valid word or letter")
            continue
        else:
            return user_input


# ---------- draw_roads ----------
def draw_roads(cols, rows, cell_w, cell_h):
    """Draw straight separator lines between rows and columns (simple roads)."""
    T.pencolor('black'); T.pensize(4) # set pen color + pensize

    for r in range(1, rows): # horizontal lines based on number of rows
        x = -400 # x value stays constant at the left edge
        y = CANVAS_H / 2 - TOP_MARGIN - r * cell_h
        move_to(x, y)
        T.setheading(0)
        T.forward(800) # across the full canvas (no left/right margins)

    for c in range(1, cols): # vertical lines based on number of columns
        x = -CANVAS_W / 2 + c * cell_w
        y = 260 # y value stays constant (at the top margin)
        move_to(x, y)
        T.setheading(270)
        T.forward(520) # moves downward until bottom margin


# ---------- draw_house_centered ----------
def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """Draw a single house based on the size centered at (cx, cy)."""

    T.pensize(0)
    # width/height
    w, h = SIZES[size_key]
    colors = THEMES[theme_key]

    if size_key == "s":
        size_key = SIZES["s"]
        move_to(cx - w / 2, cy + h / 2) # move to top left corner of the centered rectangle (body)
        # facing turtle forward to draw flat, centered rectangle
        T.setheading(0)
        if theme_key == "primary":
            T.fillcolor("red")
        else:
            T.fillcolor("#ffd1dc")
        T.begin_fill()
        for _ in range(2):
           T.forward(w); T.right(90); T.forward(h); T.right(90)
        T.end_fill()
    elif size_key == "m":
        # repeating code for "s" and replacing with "m"
        size_key = SIZES["m"] # adjusting h and w
        move_to(cx - w / 2, cy + h / 2)
        T.setheading(0)
        if theme_key == "primary":
            T.fillcolor("red")
        else:
            T.fillcolor("#ffd1dc")
        T.begin_fill()
        for _ in range(2):
           T.forward(w); T.right(90); T.forward(h); T.right(90)
        T.end_fill()
    else:
        # automatically "l" by elimination, repeat code
        size_key = SIZES["l"]
        move_to(cx - w / 2, cy + h / 2)
        T.setheading(0)
        if theme_key == "primary":
            T.fillcolor("red")
        else:
            T.fillcolor("#ffd1dc")
        T.begin_fill()
        for _ in range(2):
           T.forward(w); T.right(90); T.forward(h); T.right(90)
        T.end_fill()

    if roof_style == "triangle":
        #triangle roof- 2 lines with given apex at (cx, yT + 0.5*h) where yT = cy + h/2
        draw_line(cx - w / 2, cy + h / 2, cx, cy + h / 2 + 0.5 * h)
        draw_line(cx, cy + h / 2 + 0.5 * h, cx + w / 2, cy + h / 2 )
        if theme_key == "primary":
            # fill roof with primary
            fill_triangle((cx - w / 2, cy + h / 2), (cx, cy + h / 2 + 0.5 * h), (cx + w / 2, cy + h / 2), "blue")
        else:
            # automatically pastel
            fill_triangle((cx - w / 2, cy + h / 2), (cx, cy + h / 2 + 0.5 * h), (cx + w / 2, cy + h / 2), "#c1e1c1")
    else:
        # automatically flat roof if not triangle - draw lines based on coordinates
        draw_line(cx - w / 2, cy + h / 2, cx - w / 2, cy + h / 2 + 0.2 * h)
        draw_line(cx - w / 2, cy + h / 2 + 0.2 * h, cx - w / 2 + w, cy + h / 2 + 0.2 * h)
        draw_line(cx - w / 2 + w, cy + h / 2 + 0.2 * h, cx - w / 2 + w,  cy + h / 2 )
        if theme_key == "primary":
            # fill flat roof with primary roof color
            T.fillcolor("blue")
            move_to(cx - w / 2, cy + h / 2)
            T.begin_fill()
            T.setheading(90)
            for _ in range(2):
                T.forward(0.2 * h); T.right(90); T.forward(w); T.right(90)
            T.end_fill()
        else:
            # fill flat roof with pastel color
            T.fillcolor("#c1e1c1")
            move_to(cx - w / 2, cy + h / 2)
            T.begin_fill()
            T.setheading(90)
            for _ in range(2):
                T.forward(0.2 * h); T.right(90); T.forward(w); T.right(90)
            T.end_fill()
    move_to(cx - 0.1 * w, cy - h / 2) # bottom left of door
    T.setheading(90)
    for _ in range(2):
        # draw door
        T.forward(0.40 * h) # door height
        T.right(90)
        T.forward(0.20 * w) # door width
        T.right(90)
        if theme_key == "primary":
            # fill the door with primary color, trace over door (same code)
            T.fillcolor("gold")
            T.begin_fill()
            for _ in range(2):
                T.forward(0.40 * h); T.right(90); T.forward(0.20 * w); T.right(90)
            T.end_fill()
        else:
            # automatically pastel if not primary, fill door
            T.fillcolor("#b5d3e7")
            T.begin_fill()
            for _ in range(2):
                T.forward(0.40 * h); T.right(90); T.forward(0.20 * w); T.right(90)
            T.end_fill()

    # draw small window on the left
    T.fillcolor("yellow")
    move_to(cx - 0.1 * w, cy) # window starting point (bottom right coordinates)
    T.setheading(90)
    T.begin_fill()
    for _ in range(2):
        T.forward(0.2 * h); T.left(90); T.forward(0.3 * w); T.left(90)
    T.end_fill()


# ---------- draw_tree_near ----------
def draw_tree_near(cx, cy, size_key):
    """Draw a small tree near the house (left or right)."""
    # trunk
    w, h = SIZES[size_key]
    # trunk size (ratios)
    tw, th = w * 0.10, h * 0.40
    # place to left or right of the house randomly
    side = random.choice([-1, 1])
    tx = cx + side * (w * 0.45)
    ty = cy - h * 0.5 + th / 2
    # radius for canopy
    tree_radius = tw * 2

    move_to(tx - tw / 2, ty - th / 2)
    T.setheading(0)
    for _ in range(2):
        T.forward(tw)
        T.left(90)
        T.forward(th)
        T.left(90)

    fill_rect_center(tx, ty, tw, th, "brown") # fill the trunk brown
    move_to(tx, ty + th / 2) # bottom of circle (top of trunk)
    T.circle(tree_radius)
    fill_circle_center(tx, ty + th / 2 + tree_radius, tree_radius, "green")


# ----------  draw_village (orchestration) ----------
def draw_village(cols, rows, size_key, theme_key, roof_style):
    """Compute cell sizes, draw roads, and loop over grid to place houses/trees."""
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    draw_roads(cols, rows, cell_w, cell_h) # first draw roads

    for r in range(rows): # nested loop to draw rows and columns
        for c in range(cols):
            cx = -CANVAS_W / 2 + (c + 0.5) * cell_w # center x value
            cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h # canter y value
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            draw_tree_near(cx, cy, size_key)


# ---------- main ----------
def main():
    print("Welcome to Turtle Village — Lite!")
    # prompts validated with ask_choice_int and ask_choice_str
    cols = ask_choice_int("How many houses per row?", [2, 3])
    rows = ask_choice_int("How many rows?", [2])
    size_key = ask_choice_str("House size", ["S","M","L"])
    theme_key = ask_choice_str("Color theme", ["pastel","primary"])
    roof_style = ask_choice_str("Roof type", ["triangle","flat"])

    # window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    draw_village(cols, rows, size_key, theme_key, roof_style)
    #finalize
    T.tracer(True); T.hideturtle(); T.done()

if __name__ == "__main__":
    main()
