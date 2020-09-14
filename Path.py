import pygame as pg
import sys
import queue
import heapq
pg.init()
sys.setrecursionlimit(10000000)
font1=pg.font.SysFont('',15,True)
class button:
    def __init__(self,x,y,h,w,col,text):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.col=col
        self.text=text
    def draw(self,dis):
        pg.draw.rect(dis,self.col,(self.x,self.y,self.h,self.w))
        text=font.render(self.text,0,(0,0,0))
        dis.blit(text,(self.x+self.h//2,self.y+self.w//2))
    def over(self,pos):
        if pos[0]>self.x and pos[1]>self.y and pos[0]<self.h+self.x and pos[1]<self.w+self.y:
            self.col=(0,255,0)
            return 1
        else:
            self.col=(255,0,0)
            return 0
font = pg.font.SysFont('',30,True)
class box:
    def __init__(self,i,j,t,f,g,h,prx,pry):
        self.i=i
        self.j=j
        self.t=t
        self.f=f
        self.g=g
        self.h=h
        self.prx=prx
        self.pry=pry
    def draw(self):
        pg.draw.rect(dis,col[self.t],(self.i*w,self.j*w,w,w))
def neighbour(i1,j1,i,j):
    pg.draw.circle(dis,(23,185,255),(i1*w+w//2,j1*w+w//2),w//2)
    pg.display.update()
    pg.time.delay(10)
    arr[i1][j1].t=5
    arr[i1][j1].g=arr[i][j].g+1
    arr[i1][j1].h=abs(ex-i1)+abs(ey-j1)
    arr[i1][j1].f=arr[i1][j1].g+arr[i1][j1].h
    arr[i1][j1].prx,arr[i1][j1].pry=i,j
    heap.append((arr[i1][j1].f,(i1,j1)))
    heap_greedy.append((arr[i1][j1].h,(i1,j1)))
def push_neighbours(i,j):
    for c in range(4):
        i1=i+px[c]
        j1=j+py[c]
        if i1>=0 and i1<width//w and j1>=0 and j1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
            neighbour(i1,j1,i,j)
    i1,j1=i+1,j+1
    if i+1<width//w and j+1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i+1][j].t!=0 or arr[i][j+1].t!=0:
            neighbour(i1,j1,i,j)
    i1,j1=i-1,j+1
    if i-1>=0 and j+1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i-1][j].t!=0 or arr[i][j+1].t!=0:
            neighbour(i1,j1,i,j)
    i1,j1=i-1,j-1
    if i-1>=0 and j-1>=0 and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i-1][j].t!=0 or arr[i][j-1].t!=0:
            neighbour(i1,j1,i,j)
    i1,j1=i+1,j-1
    if i+1<width//w and j-1>=0 and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i+1][j].t!=0 or arr[i][j-1].t!=0:
            neighbour(i1,j1,i,j)
def reached(i,j):
    if i==ex and j==ey:
        return 1
    else:
        return 0
def path_find(s1,s2):
    if reached(s1,s2):
        draw_path()        
    else:
        draw_all()
        push_neighbours(s1,s2)
        if len(heap)==0:
            return
        heapq.heapify(heap)
        mn=heapq.heappop(heap)
        path_find(mn[1][0],mn[1][1])
def draw_lines():
    for i in range(0,width+1,w):
        pg.draw.line(dis,(0,0,0),(i,0),(i,height))
    for i in range(0,height+1,w):
        pg.draw.line(dis,(0,0,0),(0,i),(width,i))
def draw_rec():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j].draw()
def draw_all():
    dis.fill((255,255,255))
    if fs:
        arr[sx][sy].t=3
    draw_rec()
    draw_lines()
    pg.display.update()
def draw_path():
    ix=arr[ex][ey].prx
    iy=arr[ex][ey].pry
    while ix!=sx or iy!=sy:
        arr[ix][iy].t=2
        temp=ix
        ix=arr[temp][iy].prx
        iy=arr[temp][iy].pry
    arr[sx][sy].t=3
    arr[ex][ey].t=4
    draw_all()
def path_find_greedy(s1,s2):
    if reached(s1,s2):
        draw_path()
        open_set.clear()     
    else:
        draw_all()
        push_neighbours(s1,s2)
        if len(heap_greedy)==0:
            return
        heapq.heapify(heap_greedy)
        mn=heapq.heappop(heap_greedy)
        path_find_greedy(mn[1][0],mn[1][1])
def path_find_dijkstras():
    while not q.empty():
        draw_all()
        k=q.get()
        if k[0]==ex and k[1]==ey:
            draw_path()
            return
        push_neighbours_queue(k[0],k[1])
def push_neighbours_queue(i,j):
    for c in range(4):
        i1=i+px[c]
        j1=j+py[c]
        if i1>=0 and i1<width//w and j1>=0 and j1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
            neighbour_queue(i1,j1,i,j)
    i1,j1=i+1,j+1
    if i+1<width//w and j+1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i+1][j].t!=0 or arr[i][j+1].t!=0:
            neighbour_queue(i1,j1,i,j)
    i1,j1=i-1,j+1
    if i-1>=0 and j+1<height//w and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i-1][j].t!=0 or arr[i][j+1].t!=0:
            neighbour_queue(i1,j1,i,j)
    i1,j1=i-1,j-1
    if i-1>=0 and j-1>=0 and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i-1][j].t!=0 or arr[i][j-1].t!=0:
            neighbour_queue(i1,j1,i,j)
    i1,j1=i+1,j-1
    if i+1<width//w and j-1>=0 and arr[i1][j1].t!=5 and arr[i1][j1].t!=0:
        if arr[i+1][j].t!=0 or arr[i][j-1].t!=0:
            neighbour_queue(i1,j1,i,j)
def neighbour_queue(i1,j1,i,j):
    arr[i1][j1].t=5
    if arr[i][j].f+dist(i1,i,j1,j)<arr[i1][j1].f:
        arr[i1][j1].f=arr[i][j].f+dist(i,i,j1,j)
        arr[i1][j1].prx,arr[i1][j1].pry=i,j
    q.put((i1,j1))
def dist(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)
def reset():
    sx,sy,ex,ey=-1,-1,-1,-1
    arr.clear()
    heap.clear()
    heap_greedy.clear()
    for i in range(width//w):
        arr.append([])
        for j in range(height//w):
            a=box(i,j,1,1000,1000,1000,-1,-1)
            arr[i].append(a)
    open_set.clear()
    while not q.empty():
        q.get()
def rep_draw():
    dis.fill((255,255,255))
    b.draw(dis)
    b.over(pos)
    s.draw(dis)
    s.over(pos)
    G.draw(dis)
    G.over(pos)
color_dark_blue = (0, 0, 30)
color_blue = (255,255,200)
color_light_blue = (23,185,193)
color_green = (75, 229, 137)
color_red = (229, 42, 60)
color_purple = (96,251,247)
col=[]
col.append(color_dark_blue)
col.append(color_blue)
col.append(color_light_blue)
col.append(color_green)
col.append(color_red)
col.append(color_purple)
width=800
height=600
w=10
px=(0,-1,1,0)
py=(-1,0,0,1)
dis=pg.display.set_mode((width,height))
pg.display.set_caption("Path Finder")
q=queue.Queue()
heap=[]
heap_greedy=[]
arr=[]
open_set=[]
for i in range(width//w):
    arr.append([])
    for j in range(height//w):
        a=box(i,j,1,1000,1000,1000,-1,-1)
        arr[i].append(a)
b=button(100,10,width-120,100,(255,0,0),"A* Path Finding")
s=button(100,120,width-120,100,(255,0,0),"Dijkstras Path Finding")
G=button(100,230,width-120,100,(255,0,0),"Greedy BFS")
run=True
fs=False
mp=False
algorithm=1
global sx,sy,ex,ey
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        pos=pg.mouse.get_pos()
        rep_draw()
        if mp==False:
            rep_draw()
            if pg.mouse.get_pressed()[0]:
                if b.over(pos):
                    algorithm=1
                if s.over(pos):
                    algorithm=2
                elif G.over(pos):
                    algorithm=3
                mp=True
        else:
            if pg.mouse.get_pressed()[0]:
                arr[pos[0]//w][pos[1]//w].t=0
            if pg.mouse.get_pressed()[2]:
                arr[pos[0]//w][pos[1]//w].t=1
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_s:
                    arr[pos[0]//w][pos[1]//w].t=3
                    sx = pos[0]//w
                    sy=pos[1]//w
                    arr[sx][sy].f,arr[sx][sy].g,arr[sx][sy].h=0,0,0
                    fs=True
                    q.put((sx,sy))
                if event.key==pg.K_e:
                    arr[pos[0]//w][pos[1]//w].t=4
                    ex=pos[0]//w
                    ey=pos[1]//w
                if event.key==pg.K_SPACE:
                    if algorithm==1:
                        path_find(sx,sy)
                    elif algorithm==2:
                        path_find_dijkstras()
                    elif algorithm==3:
                        path_find_greedy(sx,sy)
                if event.key==pg.K_r:
                    reset()
                    fs=False
                    mp=False
            draw_all()
        pg.display.update()
pg.quit()
