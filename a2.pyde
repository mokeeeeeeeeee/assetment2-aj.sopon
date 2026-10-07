# note for aj.sopon : I use thonny with py5 plug in, some built in function name may be strange :)
import random
row=8
column=10
sizee=40

colour_possible=['#FF0066','#00FFCC','#0099FF','#FFCC00'] # red green blue yellow
colour_for_paint='N/A'
colour_objective='N/A'
status='PLAYING'
max_chance=12
grid=[]
datafile='saveloaddata.txt'

def init_game(): #finished flowchart
    #no parameter
    #return none
    global grid,colour_objective,status,max_chance
    grid=[]
    colour_objective=colour_possible[random.randint(0,3)]
    status='PLAYING'
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
    
def spread(x,y,target_colour,new_colour): #flowchart
    #parameter coordinate x(int), coordinate y(int), target_colour(str), new_colour(str)
    #return none
    global grid
    if target_colour == new_colour:
        return
    
    colour_spread=[[x,y]]
    while len(colour_spread)>0:
        checking_x,checking_y=colour_spread.pop()
        if checking_x < 0 or checking_x >= row or checking_y < 0 or checking_y >= column: #out of index check
            continue
        if grid[checking_x][checking_y] != target_colour:
            continue
        grid[checking_x][checking_y]=new_colour
        colour_spread.append([checking_x-1,checking_y])
        colour_spread.append([checking_x,checking_y-1])
        colour_spread.append([checking_x+1,checking_y])
        colour_spread.append([checking_x,checking_y+1])
    
def check_win(): #finsihed flowchart
    #no parameter
    #return bool
    global status
    if max_chance < 1:
        status='LOSE'
    j=0
    while j<row: #8
        i=0
        while i<column: #10
            if grid[j][i] != colour_objective:
                return False
            i+=1
        j+=1
    status='WIN'
    return True

def change_colour(x,y,new_colour): #finsihed
    #parameter coordinate x(int), coordinate y(int), new_colour(str)
    #return none
    global max_chance
    max_chance-=1
    check_win()

def get_colour_fill(colour): #finished
    #parameter colour(str)
    #return none
    global colour_for_paint
    colour_for_paint=colour

def draw_hud(): #finished 
    #no parameter
    #return none
    fill(0)
    text(f'Target color : {colour_translate(colour_objective)}   |   Turn left : {max_chance}  |  Status : {status}',10,340)
    text(f'Press R : Reload or reset game  |  Press S : Save game  |  Press L : Load game',10,420)
    no_fill()

def mouse_pressed():
    #no parameter
    #return none
    if status == 'LOSE' or status == 'WIN':
        return
    
    if (mouse_x >= 80 and mouse_x<=360) and (mouse_y >= 360 and mouse_y <= 400): # select color grid #finished
        if (mouse_x >= 80 and mouse_x<=120) and (mouse_y >= 360 and mouse_y <= 400):# red
            get_colour_fill('#FF0066')
        elif (mouse_x >= 160 and mouse_x<=200) and (mouse_y >= 360 and mouse_y <= 400):# green
            get_colour_fill('#00FFCC')
        elif (mouse_x >= 240 and mouse_x<=280) and (mouse_y >= 360 and mouse_y <= 400):# blue
            get_colour_fill('#0099FF')
        elif (mouse_x >= 320 and mouse_x<=360) and (mouse_y >= 360 and mouse_y <= 400):# yellow
            get_colour_fill('#FFCC00')
            
    if colour_for_paint == 'N/A':
        return
    
    if (mouse_x >= 0 and mouse_x<=400) and (mouse_y >= 0 and mouse_y <= 320): #game grid #correct
        j=0
        while j<row: #8
            i=0
            while i<column: #10
                if (mouse_x >= i*40 and mouse_x <= (1+i)*40) and (mouse_y >= j*40 and mouse_y <= (1+j)*40):
                    if grid[j][i] == colour_for_paint:
                        return
                    spread(j,i,grid[j][i],colour_for_paint)
                    change_colour(mouse_x,mouse_y,colour_for_paint)
                i+=1
            j+=1
        
def save_game(moves_left,target_final_color,game_state,board): #finished
    #parameter moves_left(int), target_final_color(str), game_state(str), board(2d array(list))
    #return none
    try:
        file=open(datafile,'w')
        file.write(f'{str(moves_left)}\n')
        file.write(f'{colour_translate(target_final_color).upper()}\n')
        file.write(f'{game_state}\n')
        file.write(f'{colour_translate(colour_for_paint).upper()}\n')
        j=0
        while j<row: #8
            i=0
            grid_row=[]
            while i<column: #10
                file.write(colour_translate(grid[j][i]).upper())
                if i<9:
                    file.write(',')
                i+=1
            file.write('\n')
            j+=1
        file.close()
    except FileNotFoundError:
        text(f'{datafile} not found',10,355)

def load_game(): #finished
    #no parameter 
    #return none
    global max_chance,colour_objective,status,grid,colour_for_paint
    data=[]
    try:
        with open(datafile,'r') as file: #read file
            for i in file:
                data.append(i.strip())
        max_chance=int(data[0])
        colour_objective=reverse_translate(data[1])
        status=data[2]
        colour_for_paint=reverse_translate(data[3])
        i=0
        while i<4: #remove number and str remain only list of color
            data.remove(data[0])
            i+=1
            
        i=0
        while i<8: #split comma to change array 1d to 2d
            data[i]=data[i].split(',')
            i+=1;

        j=0 #change color from saveloaddata
        while j<row: #8
            i=0
            while i<column: #10
                grid[j][i]=reverse_translate(data[j][i])
                i+=1
            j+=1
        
    except FileNotFoundError:
        text(f'{datafile} not found',10,355)
        
def key_pressed(): #finished
    #no parameter
    #return none
    if key.lower() == 's':
        save_game(max_chance,colour_objective,status,grid)
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
    else:
        return 'N/A'

def reverse_translate(colour): #finished
    if colour.lower() == 'green':
        return '#00FFCC'
    elif colour.lower() == 'blue':
        return '#0099FF'
    elif colour.lower() == 'yellow':
        return '#FFCC00'
    elif colour.lower() == 'red':
        return '#FF0066'
    else:
        return 'N/A'
    
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
