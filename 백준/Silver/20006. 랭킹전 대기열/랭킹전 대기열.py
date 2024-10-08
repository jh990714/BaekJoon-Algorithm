import sys

input = sys.stdin.readline

rooms = []

p, m = map(int, input().split())

for _ in range(p):
    input_l_n = input().split()

    level, name = int(input_l_n[0]), input_l_n[1]
    check = False

    for room in rooms:
        if len(room) >= m:
            continue
        
        if room[0][0] - 10 <= level <= room[0][0] + 10:
            room.append((level, name))
            check = True

            break
            
    if not check:
        rooms.append([(level, name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    sorted_room = sorted(room, key=lambda x: x[1])
    for player in sorted_room:
        print(*player)