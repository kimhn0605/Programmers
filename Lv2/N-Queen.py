# 유망 함수 
def Promising(pan, y, depth) :    
  for i in range(depth) :                               # depth 전까지 행을 돌면서
    if y == pan[i] or (depth-i == abs(y-pan[i])):       # 같은 열에 퀸이 존재하는지, 또는 대각선에 퀸이 존재하는지 확인
      return False                                      # 둘 중 하나라도 해당된다면 False 반환
  return True

# 재귀 함수
def Nqueen(n, pan, depth) :
  global answer  
  
  if depth == n :                       # depth 가 n 과 같게 된다면
    answer += 1                             # 모든 조건을 충족한거니까 answer += 1
  else :                                # 그게 아니라면
    for y in range(n) :                     # 모든 열 (y) 을 순회하면서
      if Promising(pan, y, depth) :         # Promising 함수 호출하여 조건 판단
        pan[depth] = y                      # 유망하다고 생각되면 해당 열 번호 (y) 를 pan[depth] 에 저장
        Nqueen(n, pan, depth+1)             # Nqueen 함수 재귀 호출
            
def solution(n):    
  global answer
  answer = 0
  pan = [0] * n             # pan : 가로 (세로) 길이만큼 0 으로 초기화시킨 1차원 배열
  Nqueen(n, pan, 0)         # 초기 depth 는 0 으로 호출
  
  return answer
