def solution(board, moves):
    
    answer = 0
    box = []
    li = [[0]*len(board[0]) for _ in range(len(board))]
    
    # 열별로 나열
    for i in range(len(board[0])) :
        for k in range(len(board)) :
            li[i][k] = board[k][i]

    for move in moves :
        while (li[move-1][0] == 0) :
            li[move-1].pop(0)
            
        if len(box) >= 1 and box[-1] == li[move-1][0] :
            del box[-1]
            del li[move-1][0] 
            answer += 2
            
        else :
            box.append(li[move-1][0])
            del li[move-1][0]
            
    return answer
