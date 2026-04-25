class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #clean
        #holy shit i tried to do it manually but i can just do this 
        arr_process = [c.lower() for c in s if c.isalnum()]

        ss = "".join(arr_process)

        #do palindrome check

        l =0 
        r = len(ss) - 1

        while l < r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1

        return True