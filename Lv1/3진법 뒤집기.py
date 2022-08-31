def solution(n):
    answer = 0
    string = ''
    qu = n
    
    while (qu != 0) :
        string += str(qu % 3)
        qu //= 3  
        
    string = string[::-1].rstrip("0")
    for i in range(len(string)) :  
        answer += pow(3, i) * int(string[i])
        
    return answer