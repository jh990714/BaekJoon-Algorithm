def solution(n, k, coins):
    result = 0

    for coin in reversed(coins):
        result += k // coin
        k = k % coin

    print(result)

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    solution(n, k, coins)