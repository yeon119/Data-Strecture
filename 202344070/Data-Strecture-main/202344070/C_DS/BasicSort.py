
#선택정렬 가장 작은수를 이동

def selection_sort(A):
    n = len(A)

    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if(A[j]<A[least]):
                least=j
            A[i],A[least] = A[least], A[i]
            printStep(A,i+1)

def printStep(arr, val):
    print( "Step %2d = " % val,end='')
    print(arr)



#삽입 정렬 == key 보다 큰 값이 있다면 오른쪽으로 이동 key 왼쪽의 값을 비교
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A,i)

#버블정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0, -1):
        bChange = False
        for j in range(i):
            if(A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChange = True
        if not bChange:
            break
        printStep(A,n-1)

        

#테스트
if __name__ =="__main__":
    A = [5,3,8,4,9,1,6,2,7]

    print('original : ', A)
    # selection_sort(A)
    # insertion_sort(A)
    # print("insertion_sort : ", A)
    bubble_sort(A)
    print("bubble_sort : ", A)




