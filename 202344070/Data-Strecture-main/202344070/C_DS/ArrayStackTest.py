from ArrayStack import ArrayStack

s = ArrayStack(100)


msg = input("문자열 입력 : ")

for c in msg:
    s.push(c)

print("입력 문자열 출력 : " , end='')
while not s.isEmpty(): # 스택이 다 비기 직전까지
    print(s.pop(),end='')
print()





