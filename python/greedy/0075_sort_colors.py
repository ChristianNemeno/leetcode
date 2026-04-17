class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count = [0,0,0]
        for num in nums:
            count[num] += 1

        i = 0
        for color in range(3):
            # we re going to repeat color count times
            for _ in range(count[color]):
                nums[i] = color 
                i += 1
        





        