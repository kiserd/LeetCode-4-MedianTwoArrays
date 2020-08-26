# Author: Donald Logan Kiser
# Date: 08/25/2020
# Description: Initial attempt at LeetCode problem 4

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # create a couple helper vars to make code more readable
    len1 = len(nums1)
    len2 = len(nums2)
    len_total = len1 + len2
    nums1_beg = nums1[0]
    nums1_end = nums1[len1 - 1]
    nums2_beg = nums2[0]
    nums2_end = nums2[len2 - 1]
    

