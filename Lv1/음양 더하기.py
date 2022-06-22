def solution(absolutes, signs):
    answer = 0    # 누적 합계 저장할 변수
    
    for i in range(len(absolutes)) :
        # 불리언 첫 문자는 대문자로
        if signs[i] == True :        
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer