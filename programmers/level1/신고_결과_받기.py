"""
2022-07-03
Level 1. 신고 결과 받기
"""

# 내가 구현한 코드
def solution(id_list, report, k):
    id_index = {}
    for index, id in enumerate(id_list):
        id_index[id] = index

    receive_id_indexes = {}
    for report_ids in report:
        give_id, receive_id = report_ids.split(' ')
        receive_id_index = id_index[receive_id]
        give_id_index = id_index[give_id]
        if not receive_id_indexes.get(receive_id_index):
            receive_id_indexes[receive_id_index] = [give_id_index]
        else:
            receive_id_indexes[receive_id_index].append(give_id_index)

    answer = [0 for _ in range(len(id_list))]
    for _, give_id_indexes in receive_id_indexes.items():
        give_id_indexes_remove_duplicate = set(give_id_indexes)
        if len(give_id_indexes_remove_duplicate) < k:
            continue
        for give_id_index in give_id_indexes_remove_duplicate:
            answer[give_id_index] += 1

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)


# Best Practice
def solution(id_list, report, k):
    answer = [0] * len(id_list)

    # dictionary 초기화 방법
    reports = {x: 0 for x in id_list}

    # 중복을 아예 report 에서 진행
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
