#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Easy to understand: recursively.
    # Just like get permute for distinct numbers.
    def permuteUnique(self, nums):
        ans = []
        nums.sort()
        self.dfs(nums, 0, ans)
        return ans

    def dfs(self, num, begin, ans):
        if begin == len(num) - 1:
            ans.append(num)
            return

        for i in range(begin, len(num)):
            if i != begin and num[i] == num[begin]:
                continue
            num[i], num[begin] = num[begin], num[i]
            # num[:], get a new copy.  Just like pass by value
            self.dfs(num[:], begin + 1, ans)


class Solution_2(object):
    '''
    1. sort nums in ascending order, add it to res;
    2. generate the next permutation of nums, and add it to res;
    3. repeat 2 until the next permutation of nums.
    '''
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        ans.append(nums[:])
        while self.nextPermutation(nums):
            ans.append(nums[:])

        return ans

    def nextPermutation(self, nums):
        length = len(nums)
        index = length - 1

        while index >= 1:
            if nums[index] > nums[index - 1]:
                for i in range(length - 1, index - 1, -1):
                    if nums[i] > nums[index - 1]:
                        nums[i], nums[index - 1] = nums[index - 1], nums[i]
                        nums[index:] = sorted(nums[index:])
                        return True
            else:
                index -= 1

        # Nums is in descending order, just reverse it.
        return False


"""
[]
[1]
[1,2,3]
[2,2,3,3]
"""
