class Node:
    def __init__(self,e,link =None):
        self.data = e
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None
        

    def isEmpty(self):
        return self.top == None
    
    # linked 에서 isFull은 아무런 의미가 없음 왜냐 아무곳이나 저장하고 그 위치만을 가르키면 되기때문에 공간을 한정하지 않음

    def isFull(self): # 물리적인 메모리 공간을 다 차지하기전까지는 의미가 없음
        return False
    
    def push(self, item):
        n = Node(item)
        n.link = self.top 
        self.top = n


    def pop(self): # 연결된 스택의 삭제연산 - > 공백이 아니면 -> 절차 1,2,3
        if not self.isEmpty():
            data = self.top.data
            self.top  = self.top.link
            return data
        
    def __str__(self):
        arr = []
        node = self.top
        while not node  == None:
            arr.append(node.data)
            node = node.link   
        return str(arr)
#테스트
if __name__ == "__main__":
    s =LinkedStack()
    print("초기 스택: ", s)

    msg = input("문자열 입력: ")

    for c in msg:
        s.push(c)
    print("스택에 삽입 : ",s )

    while not s.isEmpty():
        print(s.pop())
     