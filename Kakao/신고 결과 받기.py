def solution(id_list, reports, k):
    reports = set(reports)    # reports 배열에서 중복 제거
    li = dict()               # 딕셔너리 li : 각 유저들의 신고당한 횟수
    answer = dict()           # 딕셔너리 answer : 각 유저들의 메일받는 횟수

    send_li = []              # send_li : 신고한 유저 리스트
    receive_li = []           # receive_li : 신고당한 유저 리스트
    
    for id in id_list :       # id_list 순회하면서
        li[id] = 0            # 각 유저들의 신고당한 횟수 0 으로 초기화
        answer[id] = 0        # 각 유저들의 메일받는 횟수 0 으로 초기화
        
    for report in reports :                 # reports 배열 하나씩 순회하면서
        send, receive = report.split()      # 공백을 기준으로 split
        send_li.append(send)                # 신고한 유저 리스트에 send 추가
        receive_li.append(receive)          # 신고당한 유저 리스트에 receive 추가
        li[receive] += 1                    # 현재 receive 의 신고당한 횟수 + 1

        if li[receive] == k :                   # 신고당한 횟수가 k 번이 되었다면
            # idx : 현재 receive 를 신고했던 모든 유저들의 인덱스가 담긴 리스트
            idx = [i for i, x in enumerate(receive_li) if x == receive]
            for id in idx :                     # idx 를 하나씩 순회하면서
                answer[send_li[id]] += 1        # 현재 receive 를 신고했던 유저들의 메일받는 횟수 + 1
                
        elif li[receive] > k :                  # 신고당한 횟수가 k 번을 넘어섰다면
            answer[send] += 1                   # 현재 send 의 메일 받는 횟수만 + 1
            
    answer = list(answer.values())
    
    return answer