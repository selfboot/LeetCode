#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ Classic backtracking problem.

    One key point: for one specified number,
    just scan the number larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Here we can just use `path + [num]` to avoid modifying path, so no need to reset.
    Refer to:
    https://discuss.leetcode.com/topic/23142/python-dfs-solution
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        ans = []
        candidates.sort()
        self.dfs_search(candidates, 0, target, [], ans)
        return ans

    def dfs_search(self, candidates, start, target, path, ans):
        if target == 0:
            ans.append(path)
        else:
            for i in xrange(start, len(candidates)):
                # Cannot find the suitable sets, just return.
                num = candidates[i]
                if num > target:
                    return
                self.dfs_search(candidates, i, target - num, path + [num], ans)

"""
[]
2
[2, 3, 6, 7]
7
[1, 2, 3, 4]
10
"""
