def solution(number, k):
    stack = []
    
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
                
        stack.append(i)
    
    return ''.join(stack[:len(stack) - k])