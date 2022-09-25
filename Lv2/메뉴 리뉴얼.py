from collections import defaultdict
from itertools import combinations

# 리스트 평탄화하는 함수 (2차원 -> 1차원)
def Flatten(li):
  result = []
  for item in li :
    if type(item) == tuple :
      result += Flatten(item)
    else :
      result += [item]
  return result

def solution(orders, course):
  answer = []
  combi = defaultdict(list)
  lists = defaultdict(int)
  
  for order in orders: 
    order = sorted(order)                       # 알파벳 정렬 -> 순서 뒤바뀐 알파벳도 한 종류의 주문으로 저장
    for num in course :                           # course 에 해당하는 경우의 수를 모두 lists 에 저장
      for i in combinations(order, num) :       # combinations 모듈 사용
        lists[''.join(i)] += 1                  # 주문 횟수 누적
            
  lists = list(lists.items())                   # 인덱스 사용을 위해 리스트로 변환

  
  for li in lists :                                     # lists 를 순회하면서
    comb = combi[len(li[0])]                            # combi 딕셔너리에 { 주문 음식 가짓수 : (메뉴 조합, 주문된 횟수) } 형태로 저장
    if len(comb) == 0:      	                          # 해당 가짓수에 아직 아무것도 없는 상태일 때는 그냥 바로 저장
      combi[len(li[0])]  = li   
    elif li[1] > comb[1] :                              # 현재 메뉴 조합의 주문 횟수가 기존에 저장된 주문 횟수보다 더 많으면 바꿔치기
      combi[len(li[0])]  = li
    elif li[1] == comb[1] :                             # 기존 주문 횟수와 같을 때는 기존 것까지 포함해서 모두 저장
      combi[len(li[0])] = (comb[0], li[0]), comb[1]

  for key, val in combi.items() :           # combi 딕셔너리를 순회하면서
    if val[1] >= 2 :                        # 누적 주문 횟수가 2회 이상인 경우에만
      for v in val :                        # value 순회
        if type(v) != int :                 # answer 배열에는 주문 횟수 말고 메뉴 조합만 저장하기 위해 타입 검사
          answer.append(v)
                
  answer = sorted(Flatten(answer))          # answer 배열 평탄화 후 정렬
  return answer

# 상세 설명 : https://apfhd.tistory.com/33