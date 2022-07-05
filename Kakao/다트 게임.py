def solution(dartResult):
    answer = 0
    count = []
    option = [i for i, x in enumerate(dartResult) if x in ['*', '#']]
    bonus = [i for i, x in enumerate(dartResult) if x in ['S', 'D', 'T']]
    
    for idx in bonus :
        try :
            temp = int(dartResult[idx-2:idx])
            if dartResult[idx] == 'D' :
                count.append(10 ** 2)
            elif dartResult[idx] == 'T' :
                count.append(10 ** 3)
            else :
                count.append(10)
                
        except Exception as e:
            # print("예외 상황 발생 : ", e)
            if dartResult[idx] == 'D' :
                count.append(int(dartResult[idx-1]) ** 2)
            elif dartResult[idx] == 'T' :
                count.append(int(dartResult[idx-1])  ** 3)
            else :
                count.append(int(dartResult[idx-1]))
                
    for idx in option :
        if dartResult[idx] == "*" :
            temp = [i for i, x in enumerate(bonus) if x < idx]
            count[temp.index(temp[-1])] *= 2
            if len(temp) >= 2 :
                count[temp.index(temp[-2])] *= 2
            
        else :
            temp = [i for i, x in enumerate(bonus) if x < idx]
            count[temp.index(temp[-1])] *= (-1)
            
    answer = sum(count)
    return answer

# 상세 설명 : https://apfhd.tistory.com/17