def solution(s):
    if len(s) in [4, 6] :
        for i in s :
            try :   
                i = int(i)
            except :
                return False
    else :
        return False
    return True