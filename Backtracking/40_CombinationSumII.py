#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ Classic backtracking problem.

    One key point: for one specified number,
    just scan the number larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Here we can just use `path + [num]` to avoid modifying path, so no need to reset.
    """

    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        ans = []
        self.dfs_search(candidates, 0, target, [], ans)
        return ans

    def dfs_search(self, candidates, start, target, path, ans):
        if target == 0:
            ans.append(path)
        for i in xrange(start, len(candidates)):
            num = candidates[i]
            if num > target:
                return
            # Here skip the same `adjacent` element to avoid duplicated.
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.dfs_search(candidates, i + 1,
                            target - num, path + [num], ans)

"""
[]
1
[2, 5, 1, 4, 9]
11
[10, 1, 2, 7, 6, 1, 5]
8
"""
