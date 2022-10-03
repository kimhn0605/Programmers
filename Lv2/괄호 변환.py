# u, v 로 분리하는 함수
def Split(string) :                 
    left, right = 0, 0
    for i in range(len(string)):
        if string[i] == "(" :
            left += 1
        elif string[i] == ")" :
            right += 1
        if left == right :
            u = string[:i+1]
            v = string[i+1:] if i+1 < len(string) else ""
            return u, v
        
# 올바른 괄호 문자열인지 확인하는 함수  
def isCorrect(string) :
    stack = []
    for st in string :
        if len(stack) == 0 :
            if st == ")" :
                return False
            stack.append(st)
            continue
        if st == "(" :
            stack.append(st)
        else :
            if stack[-1] == "(" :
                stack.pop(-1)
            else :
                return False
    return True

def recurse(string) :
    result = ""
    if string == "" :                        # 1번 조건
        return "" 
    
    u, v = Split(string)                     # 2번 조건
    
    if isCorrect(u) :                        # 3번 조건
        result =  u + recurse(v)             # 3-1 조건
    else :                                   # 4번 조건
        result = "(" + recurse(v) + ")"      # 4-1 ~ 4-3 조건
        for i in range(1, len(u)-1) :        # 4-4 조건 
            if u[i] == "(" :
                result += ")"
            else :
                result += "("
    return result                            # 4-5 조건

def solution(p):
    answer = recurse(p)
    return answer 