import heapq

vertex = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix = [[0 for _ in range(13)] for _ in range(13)]

STAY, ADJACENT_STEP, DIAGONAL_STEP = 1, 2, 3


def solution(numbers: str) -> int:
    queue = []
    heapq.heappush(queue, [0, 1, 0, 1, 2, 0])
    answer = 0

    while queue:
        score, left_x, left_y, right_x, right_y, number_index = heapq.heappop(queue)
        start_left, start_right = vertex[left_x][left_y], vertex[right_x][right_y]

        if number_index >= len(numbers):
            return score if answer == 0 else min(answer, score)

        number = int(numbers[number_index]) or 11

        _left_x, _left_y, left_score = find_next(left_x, left_y, number)
        _right_x, _right_y, right_score = find_next(right_x, right_y, number)

        if left_score == right_score:
            heapq.heappush(queue, [score + left_score, _left_x, _left_y, right_x, right_y, number_index + 1])
            _set_matrix(start_left, number, left_score)

            heapq.heappush(queue, [score + right_score, left_x, left_y, _right_x, _right_y, number_index + 1])
            _set_matrix(start_right, number, right_score)

        if left_score < right_score:
            heapq.heappush(queue, [score + left_score, _left_x, _left_y, right_x, right_y, number_index + 1])
            _set_matrix(start_left, number, left_score)

        if right_score < left_score:
            heapq.heappush(queue, [score + right_score, left_x, left_y, _right_x, _right_y, number_index + 1])
            _set_matrix(start_right, number, right_score)


def find_next(x, y, destination):
    destination_x, destination_y = _get_x_y(destination)

    if destination_x == x and destination_y == y:
        _set_matrix(vertex[x][y], destination, STAY)
        return x, y, STAY

    visited = [0 for _ in range(13)]
    queue = []
    heapq.heappush(queue, [0, x, y])

    while queue:
        score, x, y = heapq.heappop(queue)
        visited[vertex[x][y]] = 1

        if vertex[x][y] == destination:
            return destination_x, destination_y, score

        if matrix[vertex[x][y]][destination] != 0:
            queue.append([score + matrix[vertex[x][y]][destination], destination_x, destination_y])
            continue

        for position_x, position_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            _x, _y = x + position_x, y + position_y
            if 0 <= _x <= 3 and 0 <= _y <= 2 and not visited[vertex[_x][_y]]:
                heapq.heappush(queue, [score + ADJACENT_STEP, _x, _y])
                _set_matrix(vertex[x][y], vertex[_x][_y], ADJACENT_STEP)

        for position_x, position_y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            _x, _y = x + position_x, y + position_y
            if 0 <= _x <= 3 and 0 <= _y <= 2 and not visited[vertex[_x][_y]]:
                heapq.heappush(queue, [score + DIAGONAL_STEP, _x, _y])
                _set_matrix(vertex[x][y], vertex[_x][_y], DIAGONAL_STEP)


def _get_x_y(number):
    _x = 0 if number <= 3 else 1 if number <= 6 else 2 if number <= 9 else 3
    _y = [2, 0, 1][number % 3]
    return (_x, _y)


def _set_matrix(x, y, score):
    matrix[x][y] = score if matrix[x][y] == 0 else min(matrix[x][y], score)
    matrix[y][x] = score if matrix[y][x] == 0 else min(matrix[y][x], score)


print(solution('0123'))
