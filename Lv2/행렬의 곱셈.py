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

#   arr1                 arr2
# [2, 3, 2]            [5, 4, 3]
# [4, 2, 4]            [2, 4, 1]
# [3, 1, 4]            [3, 1, 1]

# arr1[0][0] * arr2[0][0]
# arr1[0][1] * arr2[1][0]
# arr1[0][2] * arr2[2][0] 까지 더한 게 answer[0][0] = 22

# arr1[0][0] * arr2[0][1]
# arr1[0][1] * arr2[1][1]
# arr1[0][2] * arr2[2][1] 까지 더한 게 answer[0][1] = 22

# arr1[0][0] * arr2[0][2]
# arr1[0][1] * arr2[1][2]
# arr1[0][2] * arr2[2][2] 까지 더한 게 answer[0][2] = 11

# arr1[1][0] * arr2[0][0]
# arr1[1][1] * arr2[1][0]
# arr1[1][2] * arr2[2][0] 까지 더한 게 answer[0][1] = 36

# ....

# arr1[2][0] * arr2[0][2]
# arr1[2][1] * arr2[1][2]
# arr1[2][2] * arr2[2][2] 까지 더한 게 answer[2][2] = 14

# 곱셈 결과
# [[22, 22, 11]
# [36, 28, 18]
# [29, 20, 14]]