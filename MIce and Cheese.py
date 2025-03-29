from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k == 0:
            return sum(reward2)

        diff = []
        for i in range(len(reward1)):
            diff.append((reward1[i] - reward2[i], i))

        k_largest_diff = sorted(diff, key=lambda item: item[0])[-k:]
        largest_diff_indices = list(map(lambda item: item[1], k_largest_diff))
        reward1_sum = 0

        for i in range(len(largest_diff_indices)):
            index = largest_diff_indices[i]
            reward1_sum += reward1[index]
            reward2[index] = 0

        return reward1_sum + sum(reward2)
