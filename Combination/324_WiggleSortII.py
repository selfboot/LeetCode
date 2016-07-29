#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def wiggleSort(self, nums):
        """ Sort needed.
        Sort the array(small to big), and cut into two parts:
            For even size, left half size==right half size,
            For odd size,  left half size==right half size+1.
            (smaller part there may be one more number.)

        Then put the smaller half of the numbers on the even indexes,
        and the larger half on the odd indexes.
        Here iterate from the back of two halves,
        so that the duplicates between two parts can be split apart.

        Clear solutionm, explanation and proof can be found here:
        https://leetcode.com/discuss/76965/3-lines-python-with-explanation-proof
        """
        nums.sort()
        # half = len(nums[::2]) or half = (len(nums) + 1) // 2
        # nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


class Solution_2(object):
    def wiggleSort(self, nums):
        """ O(n)-time O(1)-space solution, no sort here.

        Find the kth smallest element, where k is the half the size (if size is even)
        or half the size+1 (if size is odd).

        Then do a three-way-partition, so that they can be split in two parts.
        Number in left parts <= those in right parts and the duplicates are around median.

        Then put the smaller half of the numbers on the even indexes,
        and the larger half on the odd indexes.
        Here iterate from the back of two halves,
        so that the duplicates between two parts can be split apart.

        According to:
        https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing
        https://discuss.leetcode.com/topic/38189/clear-java-o-n-avg-time-o-n-space-solution-using-3-way-partition
        """
        mid = len(nums[::2])
        mid_val = self.findKthLargest(nums, mid)
        self.three_way_partition(nums, mid_val)

        nums[::2], nums[1::2] = nums[mid - 1::-1], nums[:mid - 1:-1]

    def three_way_partition(self, nums, mid_val):
        """ Dutch national flag problem.

        Refer to:
        https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        """
        i, j, n = 0, 0, len(nums) - 1
        while j <= n:
            if nums[j] < mid_val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > mid_val:
                nums[n], nums[j] = nums[j], nums[n]
                n -= 1
            else:
                j += 1

    def findKthLargest(self, nums, k):
        """ Can be done in O(logn) with partition.  Here use built-in heap method.
        """
        import heapq
        return heapq.nsmallest(k, nums)[-1]

"""
[4, 5, 5, 6]
[1, 5, 1, 1, 6, 4]
[1, 3, 2, 2, 3, 1]
"""
