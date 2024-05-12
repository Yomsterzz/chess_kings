import pgzrun
import random

WIDTH = 960
HEIGHT = 540

center_x = WIDTH/2
center_y = HEIGHT/2

center = (center_x, center_y)

final_level = 10
start_speed = 5
ITEMS = ["bishop", "knight", "pawn", "rook", "queen"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bg", (0,0))
    if game_over:
        display_message("Game Over.", "Try Again")
    elif game_complete:
        display_message("You won!", "Great Job")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(extra_items):
    items_to_create = get_option_to_create(extra_items)
    new_items = create_item(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(extra_items):
    items_to_create = ["king"]
    for item in range(0,extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_item(items_to_create):
    new_items = []
    for item in items_to_create:
        option = Actor(item+"img")
        new_items.append(option)
    return new_items

def layout_items(new_items):
    num_of_gaps = len(new_items)+1
    gap_size = WIDTH/num_of_gaps
    random.shuffle(new_items)
    for index, item in enumerate(new_items):
        newposx = (index+1)*gap_size
        item.x = newposx

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = start_speed-(current_level*0.375)
        item.anchor = ("center","bottom")
        animation = animate(item, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "king" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete = True
    else: 
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(main, sub):
    screen.draw.text(main, fontsize=60, center=center, color="white")
    screen.draw.text(sub, fontsize=45, center=(center_x, center_y+50), color="white")

pgzrun.go()