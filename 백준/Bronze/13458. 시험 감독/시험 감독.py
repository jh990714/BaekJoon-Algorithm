import math

n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for room in rooms:
    if room - b > 0:
        answer += int(math.ceil((room - b) / c))
    
    answer += 1

print(answer)