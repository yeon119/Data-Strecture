#전역변수 선언(전역 변수 = 어떤 함수이든 그 값이 어디서든 통용됨)

capacity=100
size = 0
array = [None] * capacity

#isFull()

def isFull():
    return size == capacity

def isEmpty():
    if size == 0:
        return True
    else:
        return False
    
# 리스트가 비어있는지 아닌지를 알려고 하는 이유는 오버플로우, 언더플로우를 방지하기위해서

# getEntry(pos)

def getEntry(pos):
    if 0<=pos<size:
        return array[pos]
    else:
        return None


# 이 라인 위의 모든 코드들은 시간복잡도가 O(1)임 이유는 한번 실행되기떄문인데 모르면 gpt ㄱㄱ 시험에 나옴

#insert(pos, e) => 인서트는 삽입이기때문에

def insert(pos,e):
    global size # 얘를 해주지 않는다면 여기에 있는 사이즈는 로컬로 취급된다.
    if not isFull() and 0 <=pos<= size:
        for i in range(size, pos,-1):  # 뒤로 이동
            array[i] = array[i-1]  # size 는 가장 뒤의 위치를 의미하기에 리스트의 마지막을 기준으로 pos가 하나씩 빠지며 값이 작아지는걸 생각하면 i = i-1을 해야 한칸씩 뒤로 당겨올수있음
        array[pos] = e
        size += 1
    else :
        print("오버플로우 또는 pos가 유효 범위 밖에있음")
        exit()  
        
#delete(pos)

def delete(pos): # pos는 0이상이며 사이즈보다 작아야함
    global size
    if not isEmpty() and 0 <= pos < size: # 앞으로 이동
        e = array[pos]
        for i in range(pos, size-1):
            array[i+1] = array[i]
        size -=1
        return e
    else:
        print("언더플로우 또는 pos가 유효 범위 밖에있음")
        exit()
    # inssert랑 delete의 시간 복잡도는 O(n) 이것도 모르면 gptㄱㄱ
    
    
#테스트 
print("최초:", array[0:size])  # 처음 사이즈는 0이므로 빈 리스트가 출력이됨
insert(0,10)
print("삽입:", array[0:size]) # 10을 넣었기 때문에 [10]임
insert(0,20) # 0번에 있던 10이 밀리므로 [20,10]임
insert(1,30) # 1번에 30을 넣으므로 [20,30,10]
insert(3,40)
insert(2,50)
print("삽입:", array[0:size])

delete(2)
delete(3)
delete(0)
print("삭제:", array[0:size])