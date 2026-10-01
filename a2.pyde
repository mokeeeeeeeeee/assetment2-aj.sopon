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
    global grid
    grid[x][y]=new_colour
    if target_colour == grid[x][y-1]:
        grid[x][y-1]=new_colour
    if target_colour == grid[x+1][y]:
        grid[x+1][y]=new_colour
    if target_colour == grid[x][y+1]:
        grid[x][y+1]=new_colour
    if target_colour == grid[x-1][y]:
        grid[x-1][y]=new_colour

def check_win():
    #no parameter
    #return bool
    global status
    if max_chance < 1:
        status='lose'
    j=0
    while j<row: #8
        i=0
        while i<column: #10
            if grid[j][i] != colour_objective:
                return
            i+=1
        j+=1
    status='win'

def change_colour(x,y,new_colour):
    #parameter coordinate x(int), coordinate y(int), new_colour(str)
    #return none
    global max_chance
    max_chance-=1
    check_win()
    pass

def get_colour_fill(colour): #finished
    #parameter colour(str)
    #return none
    global colour_for_paint
    colour_for_paint=colour
    #print(colour_translate(colour_for_paint)) #correct

def draw_hud(): #finished ??
    #no parameter
    #return none
    fill(0)
    text(f'Target color : {colour_translate(colour_objective)}   |   Turn left : {max_chance}  |  Status : {status}',10,340)
    text(f'Press R : Reload or reset game  |  Press S : Save game  |  Press L : Load game',10,420)
    no_fill()

def mouse_pressed():
    #no parameter
    #return none
    #print(mouse_x,mouse_y)
    if status == 'lose' or status == 'win':
        return
    if (mouse_x >= 0 and mouse_x<=400) and (mouse_y >= 0 and mouse_y <= 320): #game grid #correct
        j=0
        while j<row: #8
            i=0
            while i<column: #10
                if (mouse_x >= i*40 and mouse_x <= (1+i)*40) and (mouse_y >= j*40 and mouse_y <= (1+j)*40):
                    #print(i*40,j*40,(1+i)*40,(1+j)*40,colour_translate(grid[j][i])) #correct
                    if grid[j][i] == colour_for_paint:
                        return
                    spread(j,i,grid[j][i],colour_for_paint)
                    change_colour(mouse_x,mouse_y,colour_for_paint)
                    #print(i,j,grid[j][i],colour_for_paint) #correct
                i+=1
            j+=1
        
        
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

def key_pressed(): #finished
    #no parameter
    #return none
    if key.lower() == 's':
        save_game()
    if key.lower() == 'l':
        load_game()
    if key.lower() == 'r':
        init_game()

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
        while i<column: #game grid
            fill(grid[j][i])
            rect(i*sizee,j*sizee,sizee,sizee)
            i+=1
        j+=1
    stroke(0)
    i=0
    while i<len(colour_possible): #select color 
        no_stroke()
        if colour_for_paint == colour_possible[i]:
            stroke(0)
        fill(colour_possible[i])
        rect(80+sizee*i*2,360,sizee,sizee)
        i+=1
        
    draw_hud()
