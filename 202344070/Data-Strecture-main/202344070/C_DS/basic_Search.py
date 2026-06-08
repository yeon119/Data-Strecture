#순차 탐색 알고리즘
def sequential_search(A, key,low,high):
    for i in range(low, high+1):
        print(A[i], end="")
        if A[i] == key:
            return i # 탐색 성공
    return -1 # 탐색 실패


#이진 탐색 알고리즘(순환 반복 => 자기가 자신을 다시 부름)
def binary_serach(a,key,low,high):
    if low > high:
        return -1
    middle = (low+high) //2
    print(A[middle], end="")
    if key == a[middle]:
        return middle
    elif (key < A[middle]):
        return binary_serach(A,key,low,middle-1)
    else:
        return binary_serach(A,key,middle+1,high)
    



# 테스트

if __name__ =="__main__":
    A = [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
    n = len(A)

    print("Original : " ,A)

    key = 34
    # print("순차탐색: %d" %key,sequential_search(A,key,0,n-1))
    print("이진탐색 : %d" %key, binary_serach(A,key,0,n-1) )


    key = 23
    # print("순차탐색: %d" %key,sequential_search(A,key,0,n-1)) # -1이 나오면서 탐색 실패


