import pgzrun
import random
TITLE="Recycling"
WIDTH=800
HEIGHT=600
CENTRE_X=WIDTH/2
CENTRE_Y=HEIGHT/2
CENTRE=(CENTRE_X,CENTRE_Y)
FINAL_LEVEL=10
STARTSPEED=10
ITEMS=["battery","chips","bottle","plastic"]
gameover=False
gamecomplete=False
currentlevel=1
items=[]
animations=[]

def draw():
    global items, currentlevel, gameover, gamecomplete
    screen.clear()
    screen.blit("bg",(0,0))
    if gameover:
        display_message("GAME OVER","Try Again.")
    elif gamecomplete:
        display_message("YOU WON!","Well Done.")
    else:
        for item in items:
            item.draw()

def updates():
    pass
def make_items(number_of_extra_items):
    pass
def get_option_to_create(number_of_extra_items):
    pass
def create_items(items_to_create):
    pass
def layout_items(items_to_layout):
    pass
def animate_items(items_to_animate):
    pass
def handle_game_over():
    pass
def on_mouse_down(pos):
    pass
def handle_game_complete():
    pass
def stop_animations(animations_to_stop):
    pass
def display_message(heading_text,sub_heading_text):
    pass
pgzrun.go()