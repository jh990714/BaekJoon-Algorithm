import sys

input = sys.stdin.readline

def manOp(number):
    for i in range(number, switch_len, number):
        reverseNumber(i)

def womanOp(number):
    reverseNumber(number)

    start, end = number-1, number+1
    while True:
        if not (0 < start < switch_len and 0 < end < switch_len):
            break
        
        if switch_state[start] != switch_state[end]:
            break
        
        reverseNumber(start)
        reverseNumber(end)

        start -= 1
        end += 1
    
def reverseNumber(number):
    switch_state[number] = 1 if switch_state[number] == 0 else 0 


n = int(input())
switch_state = [-1] + list(map(int, input().split()))
switch_len = len(switch_state)

for _ in range(int(input())):
    gender, number = map(int, input().split())

    if gender == 1:
        manOp(number)
    else:
        womanOp(number)

for i in range(1, switch_len):
    print(switch_state[i], end=" ")

    if i % 20 == 0:
        print()