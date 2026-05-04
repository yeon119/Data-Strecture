class CircularQueue:
    def __init__(self,capacity):
        self.capacity = 8
        self.array = [None]*self.capacity
        self.front = 0
        self.rear = 8

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity
    
    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear+1)%self.capacity
            self.array[self.rear] = e
        else: pass

    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front +1) %self.capacity
            return self.array[self.front]
        else: pass


    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front)%self.capacity]
        else: pass


    def __str__(self):
        if self.front<self.rear:
            return str(self.array[self.front+1:self.rear+1])
        else:
            return str(self.array[self.front+1:self.capacity]+ \
                       self.array[0:self.rear+1])
        

#테스트
if __name__ == "__main__":
    q= CircularQueue(8)       
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    q.enqueue("F")
    print('삽입 후 q: ',q )

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print('삭제q: ',q )

    q.enqueue("G")
    q.enqueue("H")
    q.enqueue("I")
    print('삽입 후 q: ',q )
    
