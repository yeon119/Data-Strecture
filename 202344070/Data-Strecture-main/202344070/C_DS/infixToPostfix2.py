from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

def precedence(op):
    if(op == '(' or op == ')'): 
        return 0
    elif (op == '+' or op == '-'):
        return 1
    elif (op == '*' or op == '/'):
        return 2
    else:
        return -1
    
def InfixToPostfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peak()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

#중의식을 후의식으로 변환 - 계산기 프로그램
if __name__ == "__main__":
    infix = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']

    postfix = InfixToPostfix(infix)
    result = evalPostfix(postfix)
    print('중위 표현: ', infix)
    print('후위 표현: ', postfix)
    print('계산결과: ', result)