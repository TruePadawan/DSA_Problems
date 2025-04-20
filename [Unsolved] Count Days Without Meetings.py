from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        tracker = {}
        meetings.sort(key=lambda x: x[1])
        for meeting in meetings:
            start, stop = meeting
            ranged_has_been_counted = tracker.get(start) is not None and tracker.get(stop) is not None
            if ranged_has_been_counted:
                continue
            else:
                for i in range(start, stop+1):
                    if tracker.get(i) is None:
                        tracker[i] = True
                        days -= 1
        return days