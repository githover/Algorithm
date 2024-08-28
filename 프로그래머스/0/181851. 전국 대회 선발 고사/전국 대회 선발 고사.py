def solution(rank, attendance):
    answer = 0
    attd_rank = []
    attd_idx = []
    for i in range(len(rank)):
        if attendance[i] == True:
            attd_rank.append(rank[i])
    for i in sorted(attd_rank)[:3]:
        idx = rank.index(i)
        attd_idx.append(idx)
    answer = 10000*attd_idx[0] + 100*attd_idx[1] + attd_idx[2]
    # attd_rank = []
    # attd_index = []
    # for i in range(len(rank)):
    #     if attendance[i] == True:
    #         attd_rank.append(rank[i])
    #         attd_index.append(rank.index(rank[i]))
    # print(attd_rank)
    # print(attd_index)

    return answer