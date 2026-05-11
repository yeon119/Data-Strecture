from CirecularQueue import *

map=[['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','0','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]

MAX_SIZE = 6

def isValidPos(x,y):
    if 0<= x <MAX_SIZE and 0 <= y <MAX_SIZE:
        if map[y][x]=='0' or map[y][x]=='x':
            return True
        return False
    

def BFS():
    que = CircularQueue(8)
    que.enqueue((0,1))

    while not que.isEmpty():
        here = que.dequeue()
        print(here,end="->")
        x,y = here 
        if(map[y][x] == 'x'): return True
        else:
            map[y][x] = '.'
            if isValidPos(x,y-1):que.enqueue((x,y-1)) #상
            if isValidPos(x,y+1):que.enqueue((x,y+1)) #하
            if isValidPos(x-1,y):que.enqueue((x-1,y)) #좌
            if isValidPos(x+1,y):que.enqueue((x+1,y)) #우

        print(' 현재 큐 :',que)

    return False


#테스트
result = BFS()
if result : print("==>미로 탈출 성공")
else: print("==> 미로 탈출 실패")



