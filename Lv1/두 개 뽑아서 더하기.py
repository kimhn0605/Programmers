def solution(numbers):
    answer = []
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            val = numbers[i] + numbers[j]
            if val in answer :
                continue
            else :
                answer.append(val)
    answer.sort()
    return answer