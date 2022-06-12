def solution(brown, yellow):
    total = brown + yellow
    num = []
    idx = 3
    
    while (True) :
        if total % idx == 0 :
            if idx > total // idx :
                break
            num.append([total // idx, idx])
        idx += 1
        
    for n in num :
        temp = (n[0]-2)*2 + n[1]*2
        if temp == brown :
            return [n[0], n[1]]
            break