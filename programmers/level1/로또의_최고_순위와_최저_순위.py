"""
2022-07-03
Level 1. 로또의 최고 순위와 최저 순위
"""

def solution(lottos, win_nums):
    win_num_dict = {}
    for win_num in win_nums:
        win_num_dict[win_num] = 1

    zero_count, win_num_count = 0, 0
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
        else:
            win_num_count += 1 if win_num_dict.get(lotto) else 0

    ranking = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    return [ranking[win_num_count + zero_count], ranking[win_num_count]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9]	, [20, 9, 3, 45, 4, 35]))
