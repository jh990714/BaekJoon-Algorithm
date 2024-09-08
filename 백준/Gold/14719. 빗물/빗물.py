def solution(h, w, blocks):
    result = 0
    for i in range(1, w-1):
        leftHeight = max(blocks[:i])
        rightHeight  = max(blocks[i:])

        minHeight = min(leftHeight , rightHeight)
        if minHeight > blocks[i]:
            result += minHeight - blocks[i]
    
    print(result)

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

solution(h, w, blocks)
