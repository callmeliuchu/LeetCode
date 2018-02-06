class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        i = 0
        j = 0
        arr = []
        while i<nums1_len and j<nums2_len:
            while i<nums1_len and j<nums2_len and nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i = i + 1
            while i<nums1_len and j<nums2_len and nums2[j] <= nums1[i]:
                arr.append(nums2[j])
                j = j + 1
        while i<nums1_len:
            arr.append(nums1[i])
            i = i + 1
        while j<nums2_len:
            arr.append(nums2[j])
            j = j + 1
        num_len = len(arr)
        if num_len % 2 == 0:
            return (arr[num_len//2] + arr[num_len//2-1])/2
        else:
            return arr[num_len//2]