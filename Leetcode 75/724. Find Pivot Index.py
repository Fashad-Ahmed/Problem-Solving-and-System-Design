class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        for i, j in enumerate(nums):
            right -= j
            if left == right:
                return i
            left += j
        return -1
