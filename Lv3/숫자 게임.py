def solution(A, B):
    a_i, b_i = -1, -1     # 시간 효율성 => remove 대신 포인터 사용
    answer = 0
    
    A.sort()        # 배열 A 오름차순
    B.sort()        # 배열 B 오름차순
    
    while (len(A) > 0) :
        if abs(a_i) == len(A) + 1 :     # 남아있는 A 원소가 없어서 a_i 가 범위를 벗어나면
            return answer               # answer 리턴
          
        # 끝에서부터 (큰 수부터) A 원소와 B 원소를 하나씩 비교해나가는데
        if A[a_i] >= B[b_i] :           # a 가 더 크다면         
            a_i -= 1                    # a_i - 1
            B.remove(B[0])              # a 보다 큰 수가 B 에 없다는 의미니까 버린다는 의미로 B 에서 가장 작은 수와 배치
        else :                          # b 가 더 크다면
            a_i -= 1                    # 해당 a 와 b 를 배치시켜주고 a_i, b_i 모두 - 1
            b_i -= 1
            answer += 1                 # b 가 더 큰 경우니까 answer += 1

# 상세 설명 : https://apfhd.tistory.com/27
