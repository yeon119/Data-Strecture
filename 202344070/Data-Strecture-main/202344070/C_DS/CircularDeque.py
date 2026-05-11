from CirecularQueue import * 

class CircularDeque(CircularQueue):
    def __init__(slef,capacity=10):
        super().__init__(capacity)


    def addRear(self, item):
        return self.enqueue(item)

    def deletrFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    #추가 

    def addFront(self,item):
        if not self.isFull():
            self.array[self.front]=item
            self.front=(self.front-1 +self.capacity)%self.capacity
        else:
            pass
    # 
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear-1+self.capacity) % self.capacity
        else: pass
    #

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else : pass

#test
if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2 == 0:
            dq.addRear(i)
        else:
            dq.addFront(i)

    print(" 초기 덱: ", dq)

    for i in range(2):
        dq.deletrFront()
    print(" 전단 삭제 2회:" , dq)

    for i in range(3):
        dq.deleteRear()
    print(" 후단 삭제 3회 :", dq)
        

    #우선순위 큐 : 순서에 의미가 없다
    #원래대로 했으면 하나씩 미뤄야하므로 O(n)
    # 위치만 바꿔주면 시간 복잡도는 O(1)
    # 우선순위 큐는 집합과 같이 순서가 없다 = > 선형큐라고 할수없다 => 집합도 아닌 이유는 우선순위가 같을수도 있기떄문이다