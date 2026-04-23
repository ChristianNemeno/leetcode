# O(n^2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])

        return list(res)
        

# O(n + m)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        set2 = set(nums2)
        res = set()

        for n in nums1:
            if n in set2:
                res.add(n)
            
        return list(res)
                    