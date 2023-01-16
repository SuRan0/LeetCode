def isvalid(s):
    stack = []
    a = 0
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{' or s[i] == ')' or s[i] == ']' or s[i] == '}':
            stack.append(s[i])
            a = a + 1
        if s[i] == ')' and stack[a - 2] == '(':
            stack.pop()
            stack.pop()
            a = a - 2
        elif s[i] == ']' and stack[a - 2] == '[':
            stack.pop()
            stack.pop()
            a = a - 2
        elif s[i] == '}' and stack[a - 2] == '{':
            stack.pop()
            stack.pop()
            a = a - 2
    if a == 0:
        print('true')
        return True
    else:
        print('false')
        return False


isvalid('()}')
