def StringRemove(new_id) :      # 조건 2단계 
    for id in new_id :
        # try-catch 문으로 에러 처리
        try :
            id = int(id)      # 숫자형으로 변환했을 때 오류 발생한다면 문자라는 의미
        except :
            if (ord(id) >= 97 and ord(id) <= 122) or id in ['-', '_', '.'] :
                pass
            else :
                new_id = new_id.replace(id, '')
    return new_id

def CombineDot(new_id) :        # 조건 3단계
    idx = [i for i, x in enumerate(new_id) if x == '.']
    i = 0
    while (i < len(idx)//2) :
        new_id = new_id.replace('..', '.')
        i += 1
    return new_id
  
def FinalProcess(new_id) :      # 조건 5 ~ 7단계
    if len(new_id) == 0 :
        new_id = 'a'
    elif len(new_id) >= 16 :
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <= 2 :
        while (True) :
            if len(new_id) == 3 :
                break
            else :
                new_id += new_id[-1]
    return new_id


def solution(new_id):
    id = new_id.lower()           # 조건 1단계 (소문자로 변환)
    id = StringRemove(id)         # 조건 2단계 (특수 문자 제거)
    id = CombineDot(id)           # 조건 3단계 (연속된 점 합치기)
    id = id.strip('.')            # 조건 4단계 (양쪽 점 제거)
    id = FinalProcess(id)         # 조건 5~7단계 (문자 길이 검사)

    return id

# 상세 설명 : https://apfhd.tistory.com/11