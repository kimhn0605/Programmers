def solution(n, a, b):
    round = 1
    
    while (True) :
      # 항상 짝수 번호가 이긴다고 가정하고, 홀수 번호라면 + 1
      if a % 2 == 1 :
          a += 1
      if b % 2 == 1 :
          b += 1 
          
      # A, B 둘 중 하나라도 +1 했는데 같은 번호가 되어 버린다면
      # 해당 라운드에서 경기한다는 의미이므로 break
      if a == b :
          break
      
      # 같은 번호가 아니라면 해당 라운드에서는 경기할 일 없기 때문에
      # 다음 라운드에서의 번호로 갱신 (// 2) 하고 round + 1
      a //= 2
      b //= 2
      round += 1
      
    return round
  
# 상세 설명 : https://apfhd.tistory.com/24