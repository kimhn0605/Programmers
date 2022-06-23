def solution(sizes):
    width = []          # 가로 길이 담는 배열
    height = []         # 세로 길이 담는 배열
    
    # 가로로 눕혀 수납하는 경우를 대비하여 width 에는 상대적으로 큰 값들만 저장
    for size in sizes :
        width.append(max(size))                # 주어진 가로/세로 길이 중 큰 값을 width 에 저장
        height.append(min(size))               # 주어진 가로/세로 길이 중 작은 값을 height 에 저장
        
    answer = max(width) * max(height)          # 각 배열에서 가장 큰 값을 수용할 수 있는 지갑 크기 계산
    return answer