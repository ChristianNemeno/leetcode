#I failed retry the logic of the code, so I will try to write it again.

# attempt 2 , i passed

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        if(len(s) == 0):
            return 0

        seen = set()
        res = float("-inf")
        curr = 0
        left = 0
        for right in range(len(s)):
            print("Current: " + str(curr))
            print("Letter: " + s[right])
            
            while left < len(s) and s[right] in seen:
                print("Seen?")
                seen.remove(s[left])
                left += 1
                curr -= 1
                res = max(curr,res)
            
            seen.add(s[right])
            curr += 1
            res = max(curr, res)

        return res
            