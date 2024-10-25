
k, n = map(int, input().split())

line = []

for _ in range(k):
    line.append(int(input()))

left = 1
right = max(line)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in line:
        cnt += i//mid

    if cnt >= n:
        left = mid+1
    else:
        right = mid-1

print(right)