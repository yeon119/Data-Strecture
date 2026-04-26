class ArrayList:
    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None]*capacity

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self,pos):
        if 0 < pos <= self.capacity:
            return self.array[pos]
        else:
            pass


    def insert(self,pos,e):
        if not self.isFull and 0<= pos <= self.size:
            for i in range(self.capacity -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size +=1
        else:
            pass

    def delete(self,pos):
        if not self.isEmpty and 0<= pos <=self.size:
            e = self.array[pos]
            for i in range(pos,self.size -1):
                self.array[i] = self.array[i+1]
            self.size -=1

        else:
            pass

        def replace(self,pos,e):
            if not self.isEmpty and 0 <= pos <= self.size:
                self.array[pos] = e
            else :
                pass

        def count(self,e):
            cnt = 0
            for i in range(self.size):
                if self.array[i] == e:
                    cnt += 1
            return cnt
        
        def __str__(self): # callback method array를 출력하는데 다양한 문자형이 있는데 우리는 보기 위함이기 떄문에 다 문자열로 바꿈
            return str(self.array[0:self.size]) # 슬라이싱


