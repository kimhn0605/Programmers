from collections import defaultdict

def solution(s):
  answer = len(s)
  
  for i in range(1, len(s) // 2 + 1) :        # i : 자를 문자열 개수 
    li = defaultdict(int)                     # li : 해당 문자의 연속된 개수 저장하는 딕셔너리
    result = ""                               # result : 압축된 문자열
    start = i                                 # start : 현재 문자의 시작 인덱스
    stack = []                                # stack : 들어오는 문자 저장하는 리스트 (스택)
    
    stack.append(s[:start])     # 처음 들어온 문자는 이미 스택에 저장하고 시작 
    li[s[:start]] += 1          # li 딕셔너리에 해당 문자 개수 +1
    
    while(True) :               # 압축하는 과정
      inputV = s[start:start+i]               # inputV : 현재 들어온 문자

      # 남은 문자열 개수가 i 보다 작다면
      if len(inputV) < i : 
        
        # 스택 최상단 원소 개수 확인해서 result 문자열에 추가 
        if li[stack[-1]] >= 2 :   
          result += str(li[stack[-1]]) + stack[-1]
        else :
          result += stack[-1]
            
        result += inputV             # 현재 inputV 값까지 추가한 뒤 break
        break  
      
      # 현재 inputV 값이 stack 최상단 원소랑 같지 않으면 
      if inputV != stack[-1] :     
        top = stack[-1]               # top : stack 의 최상단 원소 
        
        # top 개수 확인해서 outputV 에 저장
        if li[top] >= 2 :               
          outputV = str(li[top]) + top
        else :
          outputV = top 
            
        result += outputV       # result 문자열에 추가
        li[top] = 0             # top 개수 0 으로 초기화  
        
        stack.append(inputV)    # 현재 inputV 값 stack 에 추가하고 개수 +1
        li[inputV] += 1     
          
      else :              # 현재 inputV 값이 top 이랑 같다면 개수 +1
        li[inputV] += 1  

      start += i          # start 인덱스 갱신
    
    # 기존 answer 보다 길이가 더 작다면 바꿔치기
    if len(result) < answer :
        answer = len(result)  
  return answer

# 상세 설명 : https://apfhd.tistory.com/34

