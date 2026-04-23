class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = [x for x in set1 if x not in set2]
        list2 = [x for x in set2 if x not in set1]

        return [list1, list2]
