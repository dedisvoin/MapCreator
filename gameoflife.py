from api.lib import *

win = Window(size=[1200,900], flag=Flags.win_anyfull)

def generate_map(size):
    m = []
    for i in range(size[1]):
        k = []
        for j in range(size[0]):
            k.append(0)
        m.append(k)
    return m

MAP = generate_map([300,300])
END_MAP = copy(MAP)
TILE_SIZE = 5
GP = [0,0]

def render(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 1:
                Draw.draw_rect(win.surf, [x*TILE_SIZE+GP[0], y*TILE_SIZE+GP[1]], [TILE_SIZE], 'white')
            else:
                #Draw.draw_rect(win.surf, [x*TILE_SIZE+GP[0], y*TILE_SIZE+GP[1]], [TILE_SIZE], (100,100,100), 1)
                ...
def update():
    global MAP, END_MAP
    dummy = generate_map([300,300])
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            down = y+1
            right = x+1
            up = y-1
            left = x-1
            if down > len(MAP)-1: down = 0
            if right > len(MAP[0])-1: right = 0
            s = MAP[up][x]+MAP[up][left]+MAP[up][right]+MAP[down][x]+MAP[down][left]+MAP[down][right]+MAP[y][left]+MAP[y][right]
            if MAP[y][x] == 0:
                if s == 3:
                    dummy[y][x] = 1
            elif MAP[y][x] == 1:
                if s == 3 or s == 2:
                    dummy[y][x] = 1
                else:
                    dummy[y][x] = 0
    
    MAP = dummy
def press():
    global MAP
    mp = Mouse.pos
    if in_rect(GP, [len(MAP[0])*TILE_SIZE, len(MAP)*TILE_SIZE], mp):
        if events.GetEventById('p'):
            gp = [
                mp[0]-GP[0],
                mp[1]-GP[1],
            ]
            gp[0]-=gp[0]%TILE_SIZE
            gp[1]-=gp[1]%TILE_SIZE
            
            gp[0]//=TILE_SIZE
            gp[1]//=TILE_SIZE
            gp[0] = int(gp[0])
            gp[1] = int(gp[1])
            MAP[gp[1]][gp[0]] = 1
        if events.GetEventById('p1'):
            gp = [
                mp[0]-GP[0],
                mp[1]-GP[1],
            ]
            gp[0]-=gp[0]%TILE_SIZE
            gp[1]-=gp[1]%TILE_SIZE
            
            gp[0]//=TILE_SIZE
            gp[1]//=TILE_SIZE
            gp[0] = int(gp[0])
            gp[1] = int(gp[1])
            MAP[gp[1]][gp[0]] = 0


started = False
events = MouseEventHandler()
events.AddEvent( Mouse(Mouse.middle, Mouse.press_event,'c'))
events.AddEvent( Mouse(Mouse.right, Mouse.press_event,'p'))
events.AddEvent( Mouse(Mouse.left, Mouse.press_event,'p1'))
while win(base_color='black'):
    ms= Mouse.speed
    events.EventsUpdate()
    if events.GetEventById('c'):
        GP[0]+=ms[0]
        GP[1]+=ms[1]
    render(MAP)
    if Keyboard.key_pressed('s'):
        started = True
    if Keyboard.key_pressed('m'):
        started = False
    if started:
        update()
        
    press()