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
#알고리즘의 분석은 속도와 메모리 매번 플그램마다 저렇게 해줄순없으니까 입력 횟수에따라 시간 = 연산시에 사용됨
#입력횟수에 따른 연산횟수를 구해서 연산횟수가 적으면 좋은 알고리즘 반대면 나쁜 알고리즘
#cpu의 수행시간은 연산시간 

