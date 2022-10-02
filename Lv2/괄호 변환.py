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
    
    if string == "" :
        return "" 
    
    u, v = Split(string)  
    
    if isCorrect(u) :
        result =  u + recurse(v)   
    else :
        result = "(" + recurse(v) + ")"
        for i in range(1, len(u)-1) :
            if u[i] == "(" :
                result += ")"
            else :
                result += "("
    return result

def solution(p):
    answer = recurse(p)
    return answer 