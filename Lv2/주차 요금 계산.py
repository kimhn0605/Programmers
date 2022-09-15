from collections import defaultdict
import math

def solution(fees, records):
  answer = []
  numbers = []                    # 출차 내역 없는 경우를 대비하여 리스트 생성
  enter = defaultdict(int)        # {차량번호 : 입차 시간}
  charge = defaultdict(int)       # {차량번호 : 총 이용 시간}

  for i in range(len(records)) :
    time, num, io = records[i].split(" ")     # time : 시각, num : 차량번호, io : 내역 
    hour, minute = time.split(":")            # hour: 입/출차 시각 (시), minute: 입/출차 시각 (분)
    total = int(hour)*60 + int(minute)        # 00:00 을 기준으로 시간 계산
    
    if io == 'IN' :                   # IN 이라면
      enter[num] = total                 # 해당 차량의 입차 시간 갱신
      numbers.append(num)                # numbers 에 차량 번호 append
    else :                            # OUT 이라면
      total = total - enter[num]         # 현재 시각 - 해당 차량의 입차 시간
      charge[num] += total               # 해당 차량의 이용 시간 누적하여 charge 에 저장
      numbers.remove(num)                # numbers 에 차량 번호 remove

  for num in numbers :                # numbers 에 남아있는 차량이 있다면 
    total = 23*60+59 - enter[num]        # 출차 내역이 없다는 의미이므로 23:59 까지 시간 누적
    charge[num] += total                 # 해당 차량의 이용 시간 누적하여 charge 에 저장

  for car, total in charge.items() :                                                   # charge 를 순회하면서
    if total > fees[0] :                                                               # 총 이용 시간이 기본 시간보다 초과되었다면
      charge[car] = fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3]             # 기본 요금 + 초과된 시간만큼 단위 요금 부과
    else :                                                                             # 총 이용 시간이 기본 시간 이하라면
      charge[car] = fees[1]                                                                # 기본 요금만 부과
        
  for car, fee in sorted(charge.items()) :     # 차량 번호를 오름차순으로 정렬하여
    answer.append(fee)                         # 각 차량의 요금만 answer 에 append
    
  return answer

# 상세 설명 : https://apfhd.tistory.com/29