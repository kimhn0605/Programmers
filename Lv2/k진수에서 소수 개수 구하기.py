import math

# 소수인지 검사하는 함수
def CheckPrime(n):
  n = int(n)
  if '0' in str(n) or n == 1 :      # n 내부에 0 이 있거나 n 이 1 이라면 False 반환
    return False

  for i in range(2, math.floor(math.sqrt(n)) + 1):      # n 의 제곱근까지만 순회 => 시간 초과 해결
    if n % i == 0 :                                     # n 과 나눠떨어지는 수가 있다면 False 반환
      return False
  return True           # 소수인 경우 True 반환

def solution(n, k):
  answer = 0
  num = ''
  
  # k 진법으로 변환하는 과정
  while (True) :
    num += str(n % k)
    n //= k
    if n == 0 : 
      break
  num = num[::-1]
  
  # 조건 4 : P 처럼 소수 양쪽에 아무것도 없는 경우
  if CheckPrime(num) :  
    return answer + 1
  
  # 조건 1 ~ 3 
  else :          
    start = 0
    for i in range(len(num)) :
      if num[i] == '0' :      # i 번째 인덱스가 0 일 때
        if i != start and CheckPrime(num[start:i]) :      # i 와 start 가 다른 인덱스를 가리키고, 두 인덱스 사이에 있는 숫자가 소수라면
          answer += 1                                     # answer += 1
        start = i + 1         # i 가 가리키는 숫자 0 다음 인덱스로 start 지점 갱신
  
  if start < len(num) and CheckPrime(num[start:]) :       # 마지막 0 이후에 남은 숫자들도 소수인지 검사
    answer += 1
      
  return answer

# 상세 설명 : https://apfhd.tistory.com/30