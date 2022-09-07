from collections import defaultdict

alpha = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
li = defaultdict(int)

def solution(survey, choices):
    answer = ''
    for i in range(len(survey)) :
        if choices[i] < 4 :
            li[survey[i][0]] += (4-choices[i])
        elif choices[i] > 4 :
            li[survey[i][1]] += (choices[i]-4)
    for al in alpha :
        answer += comp(al[0], al[1])
    return answer

def comp(f, s):
    if li[f] == li[s] :
        return f
    elif li[f] < li[s] :
        return s
    else :
        return sorted([f, s])[0]
    
# 상세 설명 : https://apfhd.tistory.com/28
