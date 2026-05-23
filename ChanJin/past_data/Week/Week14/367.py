# 이건 백준 아님


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        low, high = 2, num // 2
        while low <= high:
            n = (low + high) // 2
            if n * n == num:
                return True
            elif n * n < num:
                low = n + 1
            else:
                high = n - 1
        return False
