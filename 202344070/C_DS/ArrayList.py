class ArrayList:
    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        
    def isEmpty(self):
        return self.size == 0 # 비어있는데 삭제하려면 에러가 나기떄문에 언더플로우 방지
    
    def isFull(self):
        return self.size == self.capacity # 가득차있는데 넣을려고 하면 에러남 오버플로우 방지
    
    def getEntry(self,pos):
        if 0<= pos<self.size: 
            return self.array[pos]
        else:
            return None
    
    def insert(self,pos,e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size,pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size +=1
        else :
            pass
        
    def delete(self,pos):
        if not self.isEmpty() and 0<=pos<self.size:
            e = self.array[pos]
            for i in range(pos,self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
        else:
            pass
        
    def __str__(self): # callback method array를 출력하는데 다양한 문자형이 있는데 우리는 보기 위함이기 떄문에 다 문자열로 바꿈
        return str(self.array[0:self.size]) # 슬라이싱
    
    def replace(self,pos,e):
        if not self.isEmpty() and 0 <=pos <self.size:
            self.array[pos] = e
        else:
            pass
        
    def count(self,e): 
        cnt = 0
        for i in range(0,self.size):
            if self.array[i] == e:
                cnt +1
        return cnt
        
        
        