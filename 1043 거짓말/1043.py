import sys
input = sys.stdin.readline

N, M = map(int, input().split())
known = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        if party & known:
            known = known | party

count = 0
for party in parties:
    if known.isdisjoint(party):
        count += 1

print(count)