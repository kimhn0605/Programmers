from collections import deque

def solution(s):
    answer = 0
    deq = deque(s)                         # 맨 앞에 있는 괄호를 맨 뒤로 넘겨줄 수 있도록 데크 사용
    
    for i in range(len(s)) :               # s의 길이만큼 반복
        stack = [deq[0]]                   # 초기 stack 의 최상단 괄호는 deq 의 맨 첫 번째 괄호
        
        for k in list(deq)[1:] :           # k : deq 의 두 번째 괄호부터 하나씩 순회
            if len(stack) == 0 :           # 만약 이전까지 모든 괄호들이 짝맞춰져 pop 되어 stack 에 남은 괄호가 없다면
                stack = [k]                # stack 의 최상단 괄호를 k 로 지정
                continue            
            if stack[-1] == '(' :          # 소괄호 - 올바른 괄호 문자열인지 검사
                if k == ')' :                 # 짝이 맞다면 최상단 괄호 하나만 pop 
                    stack.pop()               # 현재 k 는 아직 stack 에 추가 안 했기 때문에 pop 할 필요 X
                    continue
            elif stack[-1] == '{' :        # 중괄호 - 올바른 괄호 문자열인지 검사
                if k == '}' :
                    stack.pop()
                    continue
            elif stack[-1] == '[' :        # 대괄호 - 올바른 괄호 문자열인지 검사
                if k == ']' :
                    stack.pop()
                    continue
            stack.append(k)                # continue 인 경우 제외한 나머지 예외 상황에서는 stack 에 k 추가
            
        if len(stack) == 0 :         # stack 에 남은 괄호가 하나도 없다면
            answer += 1              # 모두 짝이 맞는 올바른 괄호 문자열이기 때문에 answer += 1
            
        deq.append(deq.popleft())    # 맨 앞에 있는 원소를 pop 하여 맨 뒤에 추가
    return answer

# 상세 설명 : https://apfhd.tistory.com/26