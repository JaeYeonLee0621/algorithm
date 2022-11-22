def solution(number, limit, power):
    numbers = [0 for _ in range(number + 1)]

    for i in range(1, number + 1):
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                if j * j == i:
                    numbers[i] += 1
                else:
                    numbers[i] += 2

            if numbers[i] > limit:
                numbers[i] = power
                break

    return sum(numbers)


print(solution(5, 3, 2))
print(solution(10, 3, 2))
