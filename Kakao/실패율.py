def solution(N, stages):
    length = len(stages)
    answer = []
    fail = dict()
    
    for i in range(1, N+1) :        # 1 ~ N 까지 반복
        cnt = stages.count(i)       # cnt : 각 스테이지별 유저 수
        
        # cnt == 0 일 때 따로 처리 안 해주면 런타임 에러
        if cnt == 0 :
            fail[i] = 0
            continue
        else :
            val = cnt / length      # 실패율 계산
            fail[i] = val           # 딕셔너리에 저장
            length -= cnt           # length 는 스테이지 도달한 유저 수
    
    # Value 값 기준으로 내림차순 정렬
    fail = sorted(fail.items(), key=lambda x:x[1], reverse=True)
    
    for i in fail :
        answer.append(i[0])
    return answer