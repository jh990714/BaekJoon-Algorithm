def solution(bandage, health, attacks):
    answer = health

    t, x, y = bandage

    attacks.sort()

    end_time = attacks[-1][0]
    pre_time = 0

    time = 0
    for time, demage in attacks:
        answer += (time - pre_time - 1) * x
        if time - pre_time - 1 >= t:
            answer += (time - pre_time - 1) // t * y
        
        answer = min(health, answer)
        answer -= demage

        if answer <= 0:
            answer = -1
            break

        pre_time = time
        

    return answer