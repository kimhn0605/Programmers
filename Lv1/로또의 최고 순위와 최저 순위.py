def solution(lottos, win_nums):
    answer = []
    min, max = 0, 0
    
    for win_num in win_nums :       # win_nums 하나씩 순회하면서
        if win_num in lottos :      # lottos 에 있는 요소와 일치한다면
            min += 1                # 최소 개수 + 1
            max += 1                # 최대 개수 + 1
            
    # lottos 배열 요소 중 0 이 모두 win_nums 에 있다고 가정하여 (최대 개수 += lottos 배열의 0 개수)
    max += lottos.count(0)          
    
    for count in [max, min] :         # 최대/최저 순위 구하기
        if count < 2 :                # 맞춘 개수가 2 개 미만이라면 무조건 6 (낙첨) 
            answer.append(6)
        else :                        # 맞춘 개수가 2 개 이상이라면
            answer.append(7-count)    # 해당 순위 출력
            
    return answer