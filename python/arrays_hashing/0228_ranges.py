    class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        a,b =0, 0 

        if len(nums) == 0 :
            return []


        for i in range(1, n):
            b = i
            print(nums[b])
            if nums[i] - nums[i-1] > 1:
                if a != i-1:
                    res.append(str(nums[a]) + "->" + str(nums[i-1]))
                    a = i
                elif a == i-1:
                    res.append(str(nums[a]))
                    a = i 
                    
        if a != b:
            res.append(str(nums[a]) + "->" + str(nums[b]))
        else:
            res.append(str(nums[a]))


        return res
        