class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])

        return list(res)
        