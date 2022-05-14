# 이분탐색

def solution(n, times) :   
    start = min(times)                # 최소 범위 : (가장 적게 걸리는 심사 시간 x 1명)
    end = max(times) * n              # 최대 범위 : (가장 많이 걸리는 심사 시간 x n명)
    
    while (start <= end) :            # end 가 start 보다 작아지기 전까지 반복
        data = 0                      # 해당 시간 내에 심사할 수 있는 인원수
        mid = (start + end) // 2      # 중간값 계산
        
        for i in times :              # 심사 시간을 하나씩 순회하면서 data 에 심사 가능한 인원수를 누적으로 추가
            if data >= n :            # 심사 가능한 인원수가 n 보다 이미 커졌다면 바로 탈출 => 시간 초과 해결
                break
            else :
                data += (mid // i)    
                
        if data >= n :                # 만약 심사 가능한 인원수가 n 이상이라면
            end = (mid - 1)           # end 값 ↓
        else :                        # 심사 가능한 인원수가 n 미만이라면
            start = (mid + 1)         # start 값 ↑

    return start
  
# 참고 자료 : https://happy-obok.tistory.com/m/10