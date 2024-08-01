import math

def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    answer = []
    current_day = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current_day:
            count += 1
        else:
            answer.append(count)
            current_day = days[i]
            count = 1

    answer.append(count)
    
    return answer
