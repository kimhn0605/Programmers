def solution(s):
    answer = []
    s = list(s)
    
    while (len(s) > 0) :
        try :         # 예외처리 -> 숫자인 경우
            s[0] = int(s[0])
            answer.append(s[0])
            del s[0]
            print(s)
        except :      # 문자인 경우
            if s[0] == 'z' :
                answer.append(0)
                del s[:4]
            elif s[0] == 'o' :
                answer.append(1)
                del s[:3]
            elif s[0] == 't' :
                if s[1] == 'w' :
                    answer.append(2)
                    del s[:3]
                else :
                    answer.append(3)
                    del s[:5]
            elif s[0] == 'f' :
                if s[1] == 'o' :
                    answer.append(4)
                    del s[:4]
                else :
                    answer.append(5)
                    del s[: 4]
            elif s[0] == 's' :
                if s[1] == 'i' :
                    answer.append(6)
                    del s[:3]
                else :
                    answer.append(7)
                    del s[:5]
            elif s[0] == 'e' :
                answer.append(8) 
                del s[:5]
            else :
                answer.append(9)
                del s[:4]
            print(s)
    result = ''
    for i in answer :
        result += str(i)
        
    return int(result)