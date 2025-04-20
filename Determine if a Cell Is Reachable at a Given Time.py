"""
Chebyshev Distance (Chessboard Distance)
If the distance is less than or equal to the seconds, return true
else false
"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        chebyshev_distance = max(abs(sx - fx), abs(sy - fy))
        if chebyshev_distance ==  0 and t == 1:
            return False
        return chebyshev_distance <= t