class DNode:
    def __init__ (self, elem,prev = None ,next=None):
        self.data=elem
        self.prev = prev
        self.next = next

class DoubleLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def isFull(self):
        return False
    
    def addFront(self,item): #전단에 추가할때
        node  = DNode(item, None, self.front)
        if(self.isEmpty()):
            self.front = self.rear = node

        else:
            self.front.prev = node
            self.front  = node    
        

    def addRear(self,item): # 후단에 추가할떄
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self): # 전단에 삭제할때
        if not self.isEmpty():
            data =self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self): # 후단에 삭제할때
        if not self.isEmpty():
            data  = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

    def __str__(self):
        arr = []
        node = self.front
        while not node == None:
            arr.append(node.data)
            node = node.next
        return str(arr)


#테스트

if __name__ == "__main__":
    dd = DoubleLinkedDeque()
    #홀수는 전단에 짝수는 후단에 삽입
    for i in range(1,11):
        if i%2 ==0:
            dd.addRear(i)
        else:
            dd.addFront(i)

    print('이중 연결 구조 리스트 삽입: ',dd)


    for i in range(2):
        dd.deleteFront()
    print("이중 연결 구조 리스트 전단 삭제 후",dd)

    for i in range(3):
        dd.deleteRear()
    print("이중  연결 구조 리스트 후단 삭제 후",dd)