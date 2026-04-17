class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l , r = 1 , x
        candid = 0
        mid = 0
        while l <= r:
            mid = (l+r) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                candid = mid
                l = mid + 1
            else:
                r = mid - 1

        return candid
        