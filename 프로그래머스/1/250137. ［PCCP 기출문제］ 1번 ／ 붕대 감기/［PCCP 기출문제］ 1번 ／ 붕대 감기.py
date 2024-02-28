def solution(bandage, health, attacks):
    answer = health

    t, x, y = bandage
    pre_time = 0
    for time, demage in attacks:
        answer += (time - pre_time - 1) * x  + (time - pre_time - 1) // t * y
        answer = min(health, answer)

        answer -= demage

        if answer <= 0:
            return -1

        pre_time = time
        
    return answer