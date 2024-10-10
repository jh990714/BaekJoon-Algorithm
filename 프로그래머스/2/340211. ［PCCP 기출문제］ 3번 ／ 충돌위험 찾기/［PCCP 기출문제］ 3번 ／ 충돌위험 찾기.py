def solution(points, routes):
    visited_count = {}

    for route in routes:
        path = findPath(points, route)

        for point in path:
            if point in visited_count:
                visited_count[point] += 1
            else:
                visited_count[point] = 1
    
    answer = 0
    for key, count in visited_count.items():
        if count >= 2:
            answer += 1

    return answer

def findPath(points, route):
    time = 0
    path = set()

    for i in range(len(route) - 1):
        start, end = points[route[i]-1], points[route[i+1]-1]
        x, y = start

        while x != end[0]:
            path.add((x, y, time))

            if x > end[0]:
                x -= 1
            else:
                x += 1

            time += 1

        while y != end[1]:
            path.add((x, y, time))

            if y > end[1]:
                y -= 1
            else:
                y += 1

            time += 1


        path.add((end[0], end[1], time))

    return path

