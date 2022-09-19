from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
  answer = [-1]                 # 라이언이 이기지 못 하는 경우를 고려하여 -1 저장
  max_gap = 0                   # max_gap : 가장 큰 점수차 저장
  
  for arrow in combinations_with_replacement(range(10, -1, -1), n):         # 중복 조합 라이브러리 사용하여 10 ~ 0 중 n 개 뽑기
    apeach, lion = 0, 0               # 어피치와 라이언 점수 각각저장
    cnt = Counter(arrow)              # 과녁 점수별로 개수 세는 Counter 라이브러리 사용
    info2 = [0 for _ in range(11)]    # info2 : 라이언 기준 과녁별 맞힌 화살 개수 (10점 ~ 0점 순서)
    
    for i in range(11) :                              # 과녁 개수만큼 순회하면서
      info2[i] = cnt[10-i]                                # cnt 에서 key 는 과녁 점수이기 때문에 (10-i) 해준 채로 info2 에 저장
      if info[i] > info2[i] :                             # 어피치 과녁 점수가 더 크다면
        apeach += (10-i)                                      # 어피치 점수 갱신
      elif info[i] < info2[i]:                            # 라이언 과녁 점수가 더 크다면
        lion += (10-i)                                        # 라이언 점수 갱신
      elif info[i] == info2[i] and info[i] != 0:          # 어피치와 라이언 점수가 동점이고 둘 다 0 점이 아닐 때
        apeach += (10-i)                                      # 어피치 점수 갱신
          
    if lion > apeach :                                # 라이언 총 점수가 더 크다면
      gap = lion - apeach                                 # gap : 라이언 점수 - 어피치 점수
      if gap > max_gap :                                  # gap 이 기존에 저장되어 있던 max_gap 값보다 크다면
        max_gap = gap                                         # max_gap 갱신
        answer = info2                                        # answer 에 현재 info2 배열 저장
      elif gap == max_gap:                                # gap 이 max_gap 값과 동일하다면
        for i in range(10, -1, -1) :                          # 10점 ~ 0점 순으로 순회하면서
          if info2[i] != 0 or answer[i] != 0 :                    # info2 와 answer 둘 중 하나라도 커지는 지점에서
              min_idx = i                                             # min_idx 에 해당 인덱스를 저장하고 break
              break
        if info2[min_idx] > answer[min_idx] :                 # 가장 낮은 점수를 더 많이 가져간 부분이 info2 라면
          answer = info2                                          # answer 갱신
    return answer
  
# 상세 설명 : https://apfhd.tistory.com/31