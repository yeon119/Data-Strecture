class ArraySet:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None]*self.capacity

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def contains(self,e):
        for i in range(self.size):
            if e == self.array[i]:
                return True
            else :
                return False
    
    def insert(self,e):
        if not self.isFull() and not self.contains(e):
            self.array[self.size] = e
            self.size += 1
        else:
            pass

    def delete(self,e):
        if not self.isEmpty() and self.contains(e):
            for i in range(self.size):
                if self.array[i] == e:
                    self.array[i] = self.array[self.size -1]
                
    def union(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])

        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC
    
    def intersection(self,setB):
        setC = ArraySet()
        for i in range(self.array):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC
    
    def equals(self,setB):
        if  not self.size == setB.size:
            return False

        for i in range(self.size):
            if not setB.contains(self.array[i]):
                return False
        return True
    def __str__(self): # 위의 조건을 모두 만족하면 True를 만족함
        return str(self.array[0:self.size]) 
        
        



        
