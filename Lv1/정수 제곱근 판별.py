def solution(n):
    idx = 1
    
    while (True) :
        if idx ** 2 == n :
            answer = (idx + 1) ** 2
            break
        elif idx ** 2 > n :
            answer = -1
            break
        else :
            idx += 1
    return answer