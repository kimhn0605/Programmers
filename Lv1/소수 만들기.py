def solution(nums):
    answer = 0
    li = []
    
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for k in range(j+1, len(nums)) :
                li.append(nums[i] + nums[j] + nums[k]) 
                
    li.sort(reverse=True)
    
    for idx in li :
        cnt = 0
        for i in range(idx-1, 1, -1) :
            if idx % i == 0 :
                cnt += 1
                break
        if cnt == 0 :
            answer += 1
    return answer
  
# 상세 설명 : https://apfhd.tistory.com/23