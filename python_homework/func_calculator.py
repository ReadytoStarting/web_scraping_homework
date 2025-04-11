def calculator(a,b,op):
    tmp = 0
    if a < b :
        tmp = a
        a = b
        b = tmp
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '*':
        return a*b
    if op == '/':
        if a !=0 and b !=0:
            return a/b
    
re = calculator(4,9,'/')
print(re)