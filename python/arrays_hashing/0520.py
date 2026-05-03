class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        another = self.mine(word)

        lowercase = True
        for c in word:
            if c.isupper():
                lowercase = False
                break

        return  another or word.isupper() or lowercase 
    
    def mine(self, s):
        l = len(s)
        if s[0].isupper():
            for i in range(1,l):
                if s[i].isupper():
                    return False
        else:
            return False
        return True
