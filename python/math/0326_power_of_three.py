class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    
        if n == 1:
            return True
        
        res = []
        i =  0
        powered = 3
        while True:
            if n in res:
                return True
            
            res.append(powered ** i)
            i += 1
            if res[-1] > n:
                break
  
        return False

        