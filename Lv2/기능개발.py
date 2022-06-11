def solution(progresses, speeds):
    answer = []
    remain = []
    
    for p in range(len(progresses)) :
        temp = (100 - progresses[p]) 
        
        if temp % speeds[p] == 0 :
            remain.append(temp // speeds[p])
        else :
            remain.append(temp // speeds[p] +1)
            
    idx = remain[0]
    cnt = 1
    
    for r in range(1, len(remain)) :
        if idx < remain[r] :
            answer.append(cnt)
            cnt = 1
            idx = remain[r]
        else :
            cnt += 1
            
        if r == len(remain)-1 :
              answer.append(cnt)
    return answer