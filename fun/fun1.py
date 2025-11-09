from time import sleep
from os import system
from random import randint
from pynput.keyboard import Key, Listener, Controller
keyboard = Controller()

SLEEPTIME = 0.1 # 时间间隔
LENTH0 = 5 # 横长度
LENTH1 = 5 # 竖直长度
DEFAULTKEY = 'w' # 默认方向
DEFAULTVALUE = "*" # 默认地图填充
SNACKHEADICON = "O" 
SNACKBODY = "+"
GAMEMAP = [[DEFAULTVALUE for _ in range(LENTH0)] for _ in range(LENTH1)]

currentkey = DEFAULTKEY
snackheadlocation = [randint(0,LENTH0-1),randint(0,LENTH1-1)] # 蛇头位置(x,y)
GAMEMAP[snackheadlocation[1]][snackheadlocation[0]] = SNACKHEADICON # 修改时应为 (y,x)
snackbodylist = []

def on_press(key:str):
    global currentkey
    print(f'{key} pressed')
    if key == Key.up:
        currentkey = "w"
    elif key == Key.down:
        currentkey = "s"
    elif key == Key.right:
        currentkey = "d"
    elif key == Key.left:
        currentkey = "a"
    else:
        currentkey = key
    
def show_map(gamemap:list[list[list]]):
    for i in gamemap:
        for j in i:
            print(j,end="")
        print("")
        

listener = Listener(on_press=on_press)
listener.start()

while(1):
    print(currentkey)
    sleep(SLEEPTIME)
    if currentkey == "w":
        pass
    pass


