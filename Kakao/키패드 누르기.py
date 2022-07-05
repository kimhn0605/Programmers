def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    
    for num in numbers :
        if num % 3 == 1 :
            answer += 'L'
            left = num
            
        elif num != 0 and num % 3 == 0 :
            answer += 'R'
            right = num
            
        else :
            temp = [[i, i+1, i+2] for i in [1, 4, 7]]
            temp2 = []
            temp.append(['*', 0, '#'])
            
            if num >= 1 and num <= 9 :
                numX = temp[(num-1)//3].index(num)
                numY = (num-1) // 3
                
            else :
                numX = 1
                numY = 3
                
            for val in [left, right] :
                if val in ['*', 0, '#'] :
                    valX = temp[3].index(val)
                    valY = 3
                    
                else :
                    valX = temp[(val-1)//3].index(val)
                    valY = (val-1) // 3
                
                dist = abs(valX - numX) + abs(valY - numY)
                temp2.append(dist)
                
            if temp2[0] < temp2[1] :
                answer += 'L'
                left = num
                
            elif temp2[1] < temp2[0] :
                answer += 'R'
                right = num
                
            else :
                answer += hand[0].upper()
                if hand == "left" :
                    left = num
                else :
                    right = num
    return answer

# 상세 설명 : https://apfhd.tistory.com/14