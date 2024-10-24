input = int(input())
cnt = 0

while input != 0:
    if input%2 == 1:
        cnt = cnt + 1

    input = input // 2

print(cnt)