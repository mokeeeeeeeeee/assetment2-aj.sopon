# note for aj.sopon : I use thonny with py5 plug in, some build in function name may be strange :)
import random
row=8
column=10
sizee=40

colour_possible=['#FF0066','#00FFCC','#0099FF','#FFCC00'] # red green blue yellow
colour_for_paint='N/A'
status='playing'
max_chance=12
grid=[]

def init_game():
    #no parameter
    #return none
    global grid
    grid=[]
    j=0
    while j<row: #8
        i=0
        grid_row=[]
        while i<column: #10
            grid_row.append(colour_possible[random.randint(0,3)])
            i+=1
        grid.append(grid_row)
        j+=1
    #print(grid) #correct

def spread(x,y,target_colour,new_colour):
    #parameter coordinate x(int), coordinate y(int), target_colour(str), new_colour(str)
    #return none
    pass

def check_win():
    #no parameter
    #return bool
    pass

def change_colour(x,y,new_colour):
    #parameter coordinate x(int), coordinate y(int), new_colour(str)
    #return none
    pass

def get_colour_fill(colour):
    #parameter colour(str)
    #return none
    pass

def draw_hud():
    #no parameter
    #return none
    pass

def mouse_pressed():
    #no parameter
    #return none
    pass

def save_game(moves_left,target_final_color,game_state,board):
    #parameter moves_left(int), target_final_color(str), game_state(str), board(?)
    #return ?
    pass

def load_game():
    #parameter ?
    #return ?
    pass

def key_pressed():
    #no parameter
    #return none
    pass

def setup():
    size(400,440)
    init_game()
    
def draw():
    background(255)
    j=0
    while j<row:
        i=0
        while i<column:
            fill(grid[j][i])
            rect(i*40,j*40,sizee,sizee)
            i+=1
        j+=1
