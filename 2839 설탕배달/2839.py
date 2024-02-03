import sys
input = sys.stdin.readline

N = int(input())
count = N//5
now_sugar = N % 5
while now_sugar <= N:
    if now_sugar % 3 == 0:
        count += now_sugar//3
        break
    else:
        now_sugar += 5
        count -= 1

print(count)