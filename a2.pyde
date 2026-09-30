# note for aj.sopon : I use thonny with py5 plug in, some build in function name may be strange :)
import random
row=8
column=10
sizee=40

colour_possible=['#FF0066','#00FFCC','#0099FF','#FFCC00'] # red green blue yellow
colour_for_paint='N/A'
colour_objective='N/A'
status='playing'
max_chance=12
grid=[]

def init_game():
    #no parameter
    #return none
    global grid,colour_objective,status,max_chance
    grid=[]
    colour_objective=colour_possible[random.randint(0,3)]
    status='playing'
    max_chance=12
    
    j=0
    while j<row: #8
        i=0
        grid_row=[]
        while i<column: #10
            grid_row.append(colour_possible[random.randint(0,3)])
            i+=1
        grid.append(grid_row)
        j+=1
    
    #print(colour_translate(colour_objective)) #correct
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
    global max_chance
    max_chance-=1
    #check_win()
    pass

def get_colour_fill(colour): #finished
    #parameter colour(str)
    #return none
    global colour_for_paint
    colour_for_paint=colour
    print(colour_translate(colour_for_paint)) #correct

def draw_hud(): #finished ??
    #no parameter
    #return none
    fill(0)
    text(f'Target color : {colour_translate(colour_objective)}   |   Turn left : {max_chance}',10,340)
    no_fill()
    pass

def mouse_pressed():
    #no parameter
    #return none
    #print(mouse_x,mouse_y)
    if (mouse_x >= 0 and mouse_x<=400) and (mouse_y >= 0 and mouse_y <= 320): #game grid #correct
        print('game')
    if (mouse_x >= 80 and mouse_x<=360) and (mouse_y >= 360 and mouse_y <= 400): # select color grid #finished
        if (mouse_x >= 80 and mouse_x<=120) and (mouse_y >= 360 and mouse_y <= 400):# red
            get_colour_fill('#FF0066')
        elif (mouse_x >= 160 and mouse_x<=200) and (mouse_y >= 360 and mouse_y <= 400):# green
            get_colour_fill('#00FFCC')
        elif (mouse_x >= 240 and mouse_x<=280) and (mouse_y >= 360 and mouse_y <= 400):# blue
            get_colour_fill('#0099FF')
        elif (mouse_x >= 320 and mouse_x<=360) and (mouse_y >= 360 and mouse_y <= 400):# yellow
            get_colour_fill('#FFCC00')
        

def save_game(moves_left,target_final_color,game_state,board):
    #parameter moves_left(int), target_final_color(str), game_state(str), board(2d array(list))
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

#-------------------- OPTIONAL FUNCTION --------------------#

def colour_translate(colour): #finished
    if colour=='#00FFCC':
        return 'green'
    elif colour=='#0099FF':
        return 'blue'
    elif colour=='#FFCC00':
        return 'yellow'
    elif colour=='#FF0066':
        return 'red'

#-------------------- OPTIONAL FUNCTION --------------------#

def setup():
    size(400,440)
    init_game()
    
def draw():
    background(255)
    j=0
    no_stroke()
    while j<row:
        i=0
        while i<column:
            fill(grid[j][i])
            rect(i*sizee,j*sizee,sizee,sizee)
            i+=1
        j+=1
    stroke(0)
    i=0
    while i<len(colour_possible):
        no_stroke()
        if colour_for_paint == colour_possible[i]:
            stroke(0)
        fill(colour_possible[i])
        rect(80+sizee*i*2,360,sizee,sizee)
        
        i+=1
        
    draw_hud()
