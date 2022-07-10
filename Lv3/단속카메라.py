def solution(routes):
    cnt = 1                              # 초기에 단속 카메라 한 대 설치
    routes = sorted(routes, key = lambda x : x[1])          # 진출 지점을 기준으로 routes 정렬
    end = routes[0][1]                   # 초기 end 값은 처음으로 나가는 차량의 진출 지점
    
    for route in routes[1:] :            # 두 번째 차량부터 순회하면서
        if route[0] > end :              # 차량의 진입 지점이 end 값보다 크다면
            cnt += 1                     # 겹치는 곳이 없다는 의미니까 cnt + 1 하고
            end = route[1]               # 해당 차량의 진출 지점으로 end 값 갱신
    return cnt