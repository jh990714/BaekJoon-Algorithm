import sys

input = sys.stdin.readline

N = int(input())
num = [*map(int, input().split())]
M = int(input())
questions = [[*map(int, input().split())] for _ in range(M)]

palindrome = [[0] * N for _ in range(N)]

for i in range(N):
   for j in range(N-i):
        start = j
        end = j + i

        if num[start] == num[end]:
            if end - start == 0: # 길이 1
                palindrome[start][end] = 1

            elif end - start == 1: # 길이 2
                palindrome[start][end] = 1
            
            else: # 길이 3이상
                if palindrome[start+1][end-1] == 1: 
                    palindrome[start][end] = 1

for s, e in questions:
    print(palindrome[s-1][e-1])