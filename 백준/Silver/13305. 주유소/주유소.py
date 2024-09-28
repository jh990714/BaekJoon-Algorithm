import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))

min_oil = city[0]
result = 0

for i in range(n-1):
    min_oil = min(min_oil, city[i])

    result += distance[i] * min_oil

print(result)