from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_li = []
    
    dict_1 = defaultdict(int)             # dict_1 : 장르별 총 재생 횟수를 내림차순 정렬한 딕셔너리
    dict_2 = defaultdict(list)            # dict_2 : 같은 장르 내 재생 횟수가 동일한 노래를 고려한 딕셔너리
    dict_3 = defaultdict(list)            # dict_3 : 노래의 재생 횟수와 인덱스를 장르별로 구분한 딕셔너리

    for i in range(len(genres)) :
        # dict_1 은 각 장르를 Key 로 지정해서 Value 에 누적 갱신
        dict_1[genres[i]] += plays[i]
        
        # dict_2 의 Key : 튜플 형태로 (장르명, 재생 횟수) 로 지정하고, 
        #           Value : append() 이용해서 인덱스를 계속 덧붙여나감.
        dict_2[(genres[i], plays[i])].append(i)

    # dict_1 을 Value 기준으로 내림차순해서 재생 횟수가 높은 장르가 맨 앞에 올 수 있도록
    dict_1 = sorted(dict_1.items(), reverse=True, key=lambda item: item[1])

    # genre_li : 총 재생 횟수가 높은 순서대로 저장해준 장르 리스트
    for i in dict_1 :
        genre_li.append(i[0])

    k = list(dict_2.keys())              # k : dict_2 의 Key 를 모아둔 리스트 => 튜플 형태 (장르명, 재생 횟수)
    v = list(dict_2.values())            # v : dict_2 의 Value 를 모아둔 리스트 => 노래의 인덱스

    for i in range(len(k)) :
        dict_3[k[i][0]].append({k[i][1] : v[i]})
        
    for gen in genre_li :
        hap = dict()
        
        # hap : dict_3 은 장르별로 Value 에 여러 개의 딕셔너리가 존재하니까
        #       하나로 합쳐주려고 update() 메서드 이용해서 합친 딕셔너리
        for i in dict_3[gen] :
            hap.update(i)
        
        # hap 을 Key 기준으로 내림차순해서 장르 안에서 제일 높은 재생 횟수와 해당 노래의 인덱스를 알아냄
        hap = sorted(hap.items(), reverse = True)
        
        # 장르별로 최대 2개까지만 노래를 수록할 수 있기 때문에
        # 제일 처음 노래의 인덱스는 무조건 저장
        answer.append(hap[0][1][0])
        
        # 수록할 나머지 노래 하나는 2가지 경우로 나눠서 아래 if-elif 문으로 작성
        if len(hap[0][1]) >= 2 :
            # 같은 장르 안에서 재생 횟수가 동일한 노래가 2개 이상일 때
            answer.append(hap[0][1][1])
        elif len(hap) >= 2 :
            # 같은 장르 안에서 재생 횟수가 여러 개일 때
            answer.append(hap[1][1][0])
    return answer

# 상세 설명 : https://apfhd.tistory.com/25