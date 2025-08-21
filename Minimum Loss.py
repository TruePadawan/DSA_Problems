import math
from typing import List, Tuple

"""
Buy low, sell next lowest
"""
def minimumLoss(price: List[int]):
    min_loss = math.inf
    augmented_prices: List[Tuple[int, int]] = []
    for index, value in enumerate(price):
        augmented_prices.append((value, index))
    augmented_prices.sort(reverse=True)
    for i in range(len(augmented_prices)):
        if i == len(augmented_prices) - 1:
            break
        price_1 = augmented_prices[i]
        price_2 = augmented_prices[i + 1]

        if price_1[0] - price_2[0] < min_loss and price_1[1] < price_2[1]:
            min_loss = price_1[0] - price_2[0]
    return min_loss
