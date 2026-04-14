class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hashmap = {}
        arr_s = s.split(" ")

        i = 0

        val_bool = False
        for c in pattern:
            if c in hashmap and i < len(arr_s):
                # if its in , i will compare it to s
                if hashmap[c] == arr_s[i]:
                    i += 1
                    continue
                else: 
                    return False
            elif i >= len(arr_s):

                return False
            
            elif c not in hashmap:

                if arr_s[i] in hashmap.values():
                    return False
                else:
                    # i will add the k v pair
                    hashmap[c] = arr_s[i]
                    i += 1

        if i < len(arr_s):
            return False        

        return True  
