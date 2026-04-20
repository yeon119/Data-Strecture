class ArrayStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if self.top == self.capacity-1:
            return True
        else:
            return False
        
    def push(self,e):
        if not self.isFull():
            self.top +=1
            self.array[self.top] = e
        else:
            pass # 오버플로우 방지

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            pass # 언더플로우 방지
    
    def peak(self): # top포인터가 가르키는곳을 보여줌
        if not self.isEmpty(): # 비어있으면 보여줄수있는게 없으니까
            return self.array[self.top]
        else:
            pass

    def __str__(self):
        return str(self.array[0:self.top+1]) # print할때 사용될 문장
    

    
