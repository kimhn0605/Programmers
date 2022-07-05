def solution(arr1, arr2):
    # arr2[0] 이 아닌 arr1[0] 으로 초기화시키면 런타임 에러
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    # i : arr1 행 개수만큼 도는 인덱스
    for i in range(len(arr1)) :
        # j : arr2 한 행 안에 들어있는 원소의 개수 (arr2 열의 개수)
        for j in range(len(arr2[0])) :
            # k : arr1 한 행 안에 들어있는 원소의 개수 (arr2 행의 개수)
            for k in range(len(arr1[0])) :
                answer[i][j] += arr1[i][k] * arr2[k][j]      
    return answer

# 상세 설명 : https://apfhd.tistory.com/8