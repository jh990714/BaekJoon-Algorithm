import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
region_price = list(map(int, input().split()))
limit_price = int(input())

left, right = 1, max(region_price)

while left <= right:
    mid = (left + right) // 2
    sum_price = 0

    for price in region_price:
        sum_price += min(price, mid)

    if sum_price > limit_price:
        right = mid - 1
    else:
        left = mid + 1

print(right)