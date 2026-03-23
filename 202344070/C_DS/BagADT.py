import time 



def insert(bag, e):
    bag.append(e) 

def remove(bag, e):
    bag.remove(e)

def contains(bag, e):
    return e in bag #bool 형태이기떄문에 return값이 있음

def count(bag):
    return len(bag) #얘도 리턴값이 있음

def numOF(bag, e):
    count = 0

    for i in bag :

        if i==e:
            count += 1

    # for i in range(len(bag)): bag의 크기만큼 
    #     if(bag[i]) == e:
    #         count+=1  인덱스의 값으로 표현하고싶다면 저렇게도 맞음

    return count

    
#프로그램 테스트

start = time.time()

myBag = []
insert(myBag,'지우개')
insert(myBag,'핸드폰')
insert(myBag,'이어폰')
insert(myBag,'볼펜')
print("내 가방속 물건 : ",myBag)

remove(myBag,'지우개')
print("내 가방속 물건 : ",myBag)

print(contains(myBag,"핸드폰")) # 결과는 True 아니면 False



print("내 가방속 물건의 갯수 :",count(myBag))

print("핸드폰의 갯수:", numOF(myBag,"핸드폰"))

end = time.time()

print("실행시간: ", end - start )
 
