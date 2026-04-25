class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """



        checkpoint = -1
        for i in range(len(nums) - 2 , -1, -1):
            if nums[i] < nums[i+1]:
                checkpoint = i
                break

        print(checkpoint)
        if checkpoint == -1:
            nums.reverse()
        else:    
            for i in range(len(nums) - 1, -1, -1):
                if nums[checkpoint] < nums[i]:
                    temp = nums[checkpoint]
                    nums[checkpoint] = nums[i]
                    nums[i] = temp
                    break

            nums[checkpoint+1:] = nums[checkpoint+1:][::-1]