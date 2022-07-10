def solution(routes):
    cnt = 1                              # 초기에 단속 카메라 한 대 설치
    routes = sorted(routes, key = lambda x : x[1])          # 진출 지점을 기준으로 routes 정렬
    end = routes[0][1]                   # 초기 end 값은 처음으로 나가는 차량의 진출 지점
    
    for route in routes[1:] :            # 두 번째 차량부터 순회하면서
        if route[0] > end :              # 차량의 진입 지점이 end 값보다 크다면
            cnt += 1                     # 겹치는 곳이 없다는 의미니까 cnt + 1 하고
            end = route[1]               # 해당 차량의 진출 지점으로 end 값 갱신
    return cnt

# 전체적인 풀이 과정
# 1. 고속도로에서 나간 지점을 기준으로 정렬
# 2. 맨 처음 차량에 대해서는 카메라 하나 설치 (세우는 위치는 나가는 지점)
# 3. 다음 차량의 진입 지점이 이전에 카메라를 세운 지점 (end) 보다 크다면 카메라를 새로 설치 (end 갱신)
