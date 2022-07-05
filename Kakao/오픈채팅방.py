def solution(record):
    li = dict()    
    answer = []
    sen = []
    
    for i, rec in enumerate(record) :
        rec = rec.split()
        op = rec[0]
        id = rec[1]

        if op == "Enter" :
            name = rec[2]
            if id in li.keys() :
                if li[id] != name :
                    idx = [i for i, x in enumerate(sen) if x[0] == id]
                    for i in idx :
                        sen[i][1] = name
            li[id] = name
            sen.append([id, name, 1])

        elif op == 'Leave' :
            name = li[id]
            sen.append([id, name, 2])
            
        else :
            name = rec[2]
            idx = [i for i, x in enumerate(sen) if x[0] == id]
            for i in idx :
                sen[i][1] = name
            li[id] = name
            
    for s in sen :
        str = ''
        if s[2] == 1 :
            str += (s[1] + '님이 들어왔습니다.')
            answer.append(str)
        elif s[2] == 2 :
            str += (s[1] + '님이 나갔습니다.')
            answer.append(str)
    return answer

# 상세 설명 : https://apfhd.tistory.com/18