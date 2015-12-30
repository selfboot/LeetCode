#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Bucket sort. Refer to:
    https://leetcode.com/discuss/48670/o-n-python-using-buckets-with-explanation-10-lines
    1. Each bucket i save one number, which satisfy val/(t+1) == i.
    2. For each number, the possible candidate can only be
    in the same bucket or the two buckets besides.
    3. Keep as many as k buckets to ensure that the difference is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        buckets = {}
        for i, val in enumerate(nums):
            bucket_num = val / (t+1)
            # Find out if there is a satisfied candidate or not.
            for b in range(bucket_num-1, bucket_num+2):
                if b in buckets and abs(buckets[b] - nums[i]) <= t:
                    return True
            # update the bucket.
            buckets[bucket_num] = nums[i]

            # Remove the bucket which is too far away.
            if len(buckets) > k:
                del buckets[nums[i - k] / (t+1)]

        return False

    # Intuitively, easy to understand, but time limit exceed.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False
        len_nums = len(nums)
        for i in range(len_nums-k):
            for j in range(i+1, i+k+1):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
    """

"""
[]
3
0
[-1,-2,-3,-3]
1
0
[1,3,5,7,1]
3
1
"""
