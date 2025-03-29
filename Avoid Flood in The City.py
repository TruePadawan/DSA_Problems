from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullLakes = {}
        ans = []
        dryDays = []
        for i in range(len(rains)):
            rain = rains[i]

            if rain == 0:
                if i != 0:
                    dryDays.append(i)
                ans.append(1)
            else:
                dayItRained = fullLakes.get(rain)
                if dayItRained is None:
                    fullLakes[rain] = i
                else:
                    # Find the earliest dry day where we can set the current lake as dried
                    if len(dryDays) == 0:
                        return []
                    for index, day in enumerate(dryDays):
                        if index == len(dryDays) - 1 and day < dayItRained:
                            return []
                        if day > dayItRained:
                            ans[day] = rain
                            dryDays.remove(day)
                            fullLakes[rain] = i
                            break
                ans.append(-1)
        return ans


test = Solution()
print(test.avoidFlood([1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3]))
