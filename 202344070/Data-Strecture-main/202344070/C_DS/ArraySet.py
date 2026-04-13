class ArraySet:
    def __init__ (self,capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None]*self.capacity
         
    def isEmpty(self): # 언더플로우 방지
        return self.size ==0
    
    def isFull(self): # 오버플로우 방지
        return self.size == self.capacity
    
    def contains(self,e): # insert 할떄 필요한거 중복여부 확인
        for i in range(self.size):
            if e == self.array[i]:
                return True
        return False # 데이터를 삽일할려면 집합에 그 값이 없어야 하기떄문에 flase여야함
    
    def insert(self,e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else:
            pass
    
    def delete(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] == self.array[self.size-1]
                self.size -= 1
                
    def union(self,setB): # 합집합 구현
        setC = ArraySet() # 새로운 구역인 c를 만들음
        for i in range(self.size):
           setC.insert(self.array[i])

        #for i in range(self.size):
            #self.array[i] == setC[i] 이 코드 나중에 다시 확인해보기 이건 SetC가 빈 배열이라 사용이 불가능함

        for i in range(setB.size):
            if not setC.contains(setB.array[i]): # 배열은 중복을 허용하지 않으르모 중복 여부를 확인한후 대입
                setC.insert(setB.array[i])

        return setC
    

    def intersect(self, setB): # 교집합 서로 중복되는 값만 포함해야함
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC
    
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]): # setB에 있는 값이 배열에 없담녀 추가해야함
                setC.insert(self.array[i])
        return setC
    
    def equals(self, setB):
        if self.size != setB.size: # 두개의 사이즈가 같은지 먼저 확인하고
            return False
        
        for i in range(self.size):
            if not setB.contains(self.array[i]): # 그 후에  서로 같은지를 확인함
                return False
            
        return True #
        # if len(self.array) == len(setB):
        #     for i in range(self.size):

            
    def __str__(self): # 위의 조건을 모두 만족하면 True를 만족함
        return str(self.array[0:self.size]) 
    

            
    
    
