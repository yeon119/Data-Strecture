from ArrayStack import ArrayStack

map = [
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','o','1','1'],
    ['1','1','1','1','1','1']
]

MAX_SIZE = 6

def isValidPos(x,y):
    if (0 <= x < MAX_SIZE)  and (0<=  y <= MAX_SIZE) :
        if map[y][x] == "0" or map[y][x] == x:
            return True
    return False


def DFS():
    print("DFS: 깊이 우선 탐색: ")
    stack = ArrayStack(100)
    stack.push((0,1)) # 입구

    while not stack.isEmpty() :
        here = stack.pop()
        print(here,end = "->" )
        (x,y) = here # 튜플 매치

        if(map[y][x] == "x"):
            return True  # 탈출성공
        else:
            map[y][x] = ','
            if isValidPos(x,y-1): stack.push(x,y-1) # 상
            if isValidPos(x,y+1): stack.push(x,y+1) # 하
            if isValidPos(x-1,y): stack.push(x-1,y) # 좌
            if isValidPos(x+1,y): stack.push(x+1,y) # 우

        print("현재스택 : " , stack)            
    return False # 탈출을 성공하지 못함


#테스트

result = DFS()

if result: print("미로 탈출 성공")

else : print("미로 탈출 실패")





            
