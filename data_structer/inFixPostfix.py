from Arraystack import ArrayStack
from EvalPost import evalPostfix

def precdence(op):
    if(op=="(" or op ==')'):
        return 0
    elif(op =="+" or op == "-"):
        return 1
    elif(op == "*" or op == "/"):
        return 2
    else:
        return-1
    

def InfixToPostfix(expr):
    s= ArrayStack(100)
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

        elif term in "+_*/":
            while not s.isEmpty():
                op = s.peek()
                if(precdence(term) <= precdence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())

    return output.append