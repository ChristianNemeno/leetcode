class Solution:
    def climbStairs(self, n: int) -> int:
        # this is a top down approach i understand this more than bottom up approach
        memo = {}

        def fn(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            
            memo[i] = fn(i-1) + fn(i-2)
            return memo[i]
    
        return fn(n)