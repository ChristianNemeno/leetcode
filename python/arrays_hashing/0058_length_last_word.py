class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0 

        right = len(s) - 1

        trueth = True
        while right >= 0:
            if s[right].isspace():
                if trueth:
                    right -= 1
                else:
                    return counter
            elif s[right].isalpha():
                trueth = False
                counter += 1
                right -=1

        return counter


        # previously i did this

        # arr = s.split()
        # return len(arr[-1]) if arr else 0