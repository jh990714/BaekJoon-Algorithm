import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))

    max_price = 0
    answer = 0

    for stock in reversed(stocks):
        if stock > max_price:
            max_price = stock
        else:
            answer += max_price - stock

    print(answer)