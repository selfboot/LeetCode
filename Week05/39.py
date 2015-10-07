#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        sol = self.sum(candidates, target)
        combinationLists = []
        for candidate in sol:
            candidate.sort()
            if candidate not in combinationLists:
                combinationLists.append(candidate)

        return combinationLists

    def sum(self, candidates, target):
        assert(target > 0)
        sol = []
        for num in candidates:
            if num > target:
                break
            elif num == target:
                sol.append([num])
            else:
                for l in self.sum(candidates, target - num):
                    num_list = []
                    num_list.append(num)
                    num_list.extend(l)
                    sol.append(num_list)

        return sol
