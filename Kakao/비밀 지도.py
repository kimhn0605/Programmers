def solution(n, arr1, arr2):
    answer = []
    n_arr1 = []
    n_arr2 = []
    
    for i in range(n) :
        b = bin(arr1[i])[2:]
        while (True) :
            if len(b) == n :
                break
            else :
                b = '0' + b
        n_arr1.append(b)
        
    for i in range(n) :
        b = bin(arr2[i])[2:]
        while (True) :
            if len(b) == n :
                break
            else :
                b = '0' + b
        n_arr2.append(b)
    
    for i in range(n) :
        temp = ''
        for k in range(n) :
            if (n_arr1[i][k] == n_arr2[i][k]) and n_arr1[i][k] == "0" :
                temp += ' '
            else :
                temp += '#'
        answer.append(temp)
    return answer

# 상세 설명 : https://apfhd.tistory.com/16