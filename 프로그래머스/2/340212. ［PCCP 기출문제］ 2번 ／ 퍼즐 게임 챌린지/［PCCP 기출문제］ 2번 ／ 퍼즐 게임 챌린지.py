def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if timeToSolve(diffs, times, mid) > limit:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
            
    return answer

def timeToSolve(diffs, times, level):
    time = 0
    time_prev = 0
    
    for i in range(len(diffs)):
        if diffs[i] <= level:
            time += times[i]
        else:
            cnt = diffs[i] - level
            time += (times[i] + time_prev) * cnt + times[i]
            
        time_prev = times[i]
        
    return time

