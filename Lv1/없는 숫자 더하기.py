def solution(numbers):
    numbers.sort()      # 주어진 배열 오름차순
    result = 0          # 리턴할 값
    i = -1              # 배열의 요소들과 비교할 인덱스값
    
    for num in numbers :    # 배열의 요소들을 하나씩 순회
        i += 1              # 인덱스 증가 후 num 과 동일한 지 비교
        while (num != i) :    # num 과 i 가 같아질 때까지 result 에 i 누적해서 저장
            result += i
            i += 1
            
    while (i != 9) :      # 만약 마지막 숫자가 9 이전에 끝났다면
        i += 1            # 인덱스 증가 후 9 가 될 때까지 누적해서 저장
        result += i
  
    return result