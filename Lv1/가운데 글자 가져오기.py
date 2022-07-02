def solution(s):
    answer = ''
    le = len(s)
    
    if le % 2 == 0 :
        return s[le//2-1:le//2+1]
    else :
        return s[le//2]