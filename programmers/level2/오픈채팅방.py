"""
2022-07-03
Level 2. 오픈채팅방
"""


def solution(records):
    nicknames, answer_commands = {}, []
    for record in records:
        commands = record.split(' ')
        answer_commands.append([commands[0], commands[1]])
        if not commands[0] == 'Leave':
            nicknames[commands[1]] = commands[2]

    answer = []
    for answer_command in answer_commands:
        command, unique_id = answer_command
        if command == 'Enter':
            answer.append(f'{nicknames[unique_id]}님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(f'{nicknames[unique_id]}님이 나갔습니다.')

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])