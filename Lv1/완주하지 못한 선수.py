def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)) :
        if i == len(completion) :            # 참가자 인원 = 완주자 인원 + 1 이용
            return participant[-1]           # 마지막 선수 이름 출력
          
        if participant[i] != completion[i] :    # 이름 달라지는 지점 -> 완주자 명단에 없다는 의미
            return participant[i]