def solution(price, money, count):
    answer = 0      # 초기 금액
    
    for i in range(1, count+1) :       # 1 ~ count 까지 순회
        answer += i*price              # 이용료의 N배 누적 합 계산
        
    if answer - money > 0 :            # 모자라는 금액이 있다면 그 차이만큼 반환
        result = answer - money
        
    else :          # 모자라는 금액이 없다면 0 반환
        result = 0
        
    return result