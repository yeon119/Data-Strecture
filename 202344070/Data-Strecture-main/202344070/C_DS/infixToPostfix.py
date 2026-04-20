from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

def precdence(op): # op는 연산자
    if(op=="(" or op ==')'):
        return 0
    elif(op =="+" or op == "-"):
        return 1
    elif(op == "*" or op == "/"):
        return 2
    else:
        return-1
    
def InfixToPostfix(expr): # expr는 중위식
    s = ArrayStack(100)
    output = []
    
    for term in expr: 
        if term in '(':  # 이 부분이 괄호에 대한 처리법
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty(): # 우선순위가 높은부분을 아웃풋에 넣는 과정
                op = s.peak()
                if(precdence(term) <= precdence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)

        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output # 최종 우후위 표기식을 반환


# 중위식을 후위식으로 변환

if __name__ == "__main__":
    infix = ['8','/','2','-','3','+','(','3','*','2',')']

    postfix = InfixToPostfix(infix)
    result = evalPostfix(postfix)

    print('중위표현 : ',infix)
    print('후위표현 : ',postfix)
    print('계산결과 : ',result)