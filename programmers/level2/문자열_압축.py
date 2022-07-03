"""
2022-07-03
Level 2. 문자열 압축
"""


def solution(s):
    answer = len(s)
    start_length = answer // 2
    for length in range(start_length, 0, -1):
        start_index = 0
        token = s[start_index:start_index + length]
        next_start_index = start_index + length
        result, loop = '', 1
        while next_start_index < len(s):
            if token == s[next_start_index:next_start_index + length]:
                loop += 1
            else:
                result += f'{"" if loop == 1 else str(loop)}{token}'
                loop, token = 1, s[next_start_index:next_start_index + length]
            next_start_index += length

        result += f'{"" if loop == 1 else str(loop)}{token}'
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
