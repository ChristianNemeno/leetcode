import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        target = int(round(math.log(n, 2)))
        l, r = 0, 30
        

        while l <= r:
            m = (l+r) // 2


            if m == target:
                return 2 ** m == n

            elif m < target:
                l = m + 1
            
            else:
                r = m - 1

        return False