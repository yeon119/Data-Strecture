class Node:
    def __init__ (self, elem, next=None):
        self.data=elem
        self.link=next
       
class LinkedQueue:
    def __init__(self):
        self.tail=None
       
    def isEmpty(self):
        return self.tail==None
   
    def isFull(self):
        return False
   
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.tail = node
            node.link=node
        else:
            node.link = self.tail.link
            self.tail.link=node
            self.tail=node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail =None
            else:
                self.tail.link = self.tail.link.link
            return data
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
        
    def size(self):
        if self.isEmpty():
            return 0 
        else:
            count = 1
            node = self.tail.link
            while not node ==  self.tail:
                count +=1
                node =node.link

            return count
        



    def __str__(self):
        arr =[]
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)
    
#테스트
if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')

    print(" 원형큐 삽입: ",q)

    print('삭제: ',q.dequeue())
    print('삭제: ',q.dequeue())
    print('삭제: ',q.dequeue())
    
    print(" 원형큐 삭제후: ",q)