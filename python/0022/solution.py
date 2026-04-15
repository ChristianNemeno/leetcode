class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        s = []
        def backtrack(curr, open, close):

            if len(curr) == n * 2:
                s.append(curr)
                return  
            
            if open < n:
                backtrack(curr + "(" , open + 1, close)
            
            if close < open:
                backtrack(curr + ")", open, close + 1)

        backtrack("", 0, 0)
        return s



        # S -> SS
        # S -> ()
        # S -> (S) 
        # S -> e         