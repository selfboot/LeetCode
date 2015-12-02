#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.get_all_paths(root, sum)

    # Find all the paths whose node's sum equals the given sum
    def get_all_paths(self, root, sum):
        paths_list = []
        if not root.left and not root.right:
            if root.val == sum:
                paths_list.append([root.val])
            return paths_list

        if root.left:
            l_paths = self.get_all_paths(root.left, sum-root.val)
            # There are paths along root.left
            if l_paths:
                for path in l_paths:
                    one_path = [root.val]
                    one_path.extend(path)
                    paths_list.append(one_path)

        if root.right:
            r_paths = self.get_all_paths(root.right, sum-root.val)
            # There are paths along root.right
            if r_paths:
                for path in r_paths:
                    one_path = [root.val]
                    one_path.extend(path)
                    paths_list.append(one_path)
        return paths_list

"""
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,3,3,3]
6
"""
