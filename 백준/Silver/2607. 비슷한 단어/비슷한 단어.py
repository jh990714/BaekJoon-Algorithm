import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

first_word = input().rstrip()
first_word_ch = defaultdict(int)
for ch in first_word:
    first_word_ch[ch] += 1

answer = 0
for _ in range(n-1):
    word = input().rstrip()
    word_ch = defaultdict(int)

    if abs(len(first_word) - len(word)) >= 2:
        continue

    for ch in word:
        word_ch[ch] += 1

    cnt = 0
    for key in set(first_word_ch.keys()).union(word_ch.keys()):
        cnt += abs(first_word_ch[key] - word_ch[key])

    if cnt <= 2:
        answer += 1

print(answer)        