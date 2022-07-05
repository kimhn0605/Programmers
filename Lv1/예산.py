def solution(d, budget):
    answer = 0
    d.sort()
    cnt = 0
    now = 0
    
    for i in d :
        if now + i > budget :
            break
        else :
            cnt += 1
            now += i
    return cnt

# 상세 설명 : https://apfhd.tistory.com/22