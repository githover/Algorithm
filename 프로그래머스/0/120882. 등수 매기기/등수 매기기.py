def solution(score):
    avg_list = []
    rank_list = []
    
    for i in range(len(score)):
        rank_list.append(0)
        avg_list.append((score[i][0] + score[i][1]) / 2)
    
    for idx, avg in enumerate(avg_list):
        for avg2 in avg_list:
            if avg < avg2:
                rank_list[idx] += 1
                
    for i in range(len(rank_list)):
        rank_list[i] += 1
        
    return rank_list