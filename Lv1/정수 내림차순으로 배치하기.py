def solution(n):
    answer = sorted(list(str(n)), reverse = True)     # 문자열로 바꿔서 내림차순 정렬
    answer = int(''.join(answer))                     # "" 형태를 없애주기 위해 정수형으로 변환
    return answer