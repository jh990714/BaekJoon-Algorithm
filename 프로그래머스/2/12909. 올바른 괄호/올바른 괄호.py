def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            
            if stack.pop() != '(':
                return False
    
    return not stack
            
        