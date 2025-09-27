from typing import List


def candies(n: int, arr: List[int]) -> int:
    result = [1] * n

    for i in range(1, n):
        prev_student = arr[i - 1]
        current_student = arr[i]

        if current_student > prev_student:
            result[i] = result[i - 1] + 1

    # The minimum candy needed is determined after considering neighbors from both sides
    for i in range(n - 2, -1, -1):
        current_student = arr[i]
        next_student = arr[i + 1]

        if current_student > next_student:
            # Increase the candy the current student gets to 1 + whatever is higher between the current candy and next candy
            result[i] = max(result[i + 1] + 1, result[i])

    return sum(result)

ratings = [1,2,3,2,1]
print(candies(len(ratings), ratings))
