capacity = 10
array = [None] * capacity
top = -1

def isEmpty(): # 언더플로우 방지
    if top == -1:
        return True
    else:
        return False
    
def isFull():
    if top == capacity-1:
        return True
    else:
        return False
    
def push(e):
    global top # 글로벌 함수를 정의해야지만 바뀐 결과값이 적용됨
    if not isFull:
        top += 1
        array[top] = e
    else:
        pass

def pop():
    global top
    if not isEmpty:
        top -= 1
        return array[top+1]
    else:
        pass # 언더플로우 방지

def peak():
    if not isEmpty():
        return array[top] # 맨 위에 있는 값을 삭제하지 않고 반환만 하는 메소드
    else:
        pass

