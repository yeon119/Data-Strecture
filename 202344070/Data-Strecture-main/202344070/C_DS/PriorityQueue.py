class PriorityQueue:
    def __init__(self,capacity = 10):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.size = 0
        

    def isEmpty(self):
        return self.size == 0


    def isFull(self):
        return  self.size == self.capacity
    

    def enqueue(self,e):
        if not self.isFull():
            self.array[self.size] = e
            self.size +=1

    def findMaxIndex(self): # 안에 있는 값보다 인덱스 번호를 알아야 값을 꺼내올수있기 떄문에 인덱스 번호를 구함
        if self.isEmpty():
            return -1
        higest = 0
        for i in range(self.size):
            if self.array[i] > self.array[higest]:
                higest = i # 인덱스 번호를 찾는거기 떄문에 i 를 넣음
        return higest
        

    def dequeue(self):
            highest = self.findMaxIndex()
            if highest != -1:
                self.size -= 1
                self.array[highest],self.array[self.size] = self.array[self.size],self.array[highest] # 튜플 사용 두 매체를 교환함
                return self.array[self.size]


    def peek(self):
        if self.isEmpty():
         highest = self.findMaxIndex()
         if highest != -1:
             return self.array[highest]
         
    def __str__(self):
        return str(self.array[0:self.size])
# 테스트

if __name__=="__main__":
    q = PriorityQueue()
    q.enqueue(34)
    q.enqueue(18)
    q.enqueue(27)
    q.enqueue(45)
    q.enqueue(15)
    print(" 우선순위큐 : ",q)

    while not q.isEmpty():
        print("Max Priority: ", q.dequeue())