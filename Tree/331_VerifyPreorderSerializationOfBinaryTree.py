#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        When there are two consecutive "#" characters on top of the stack,
        pop both of them and replace the top element on the remain stack with "#".
        """
        preorder = preorder.split(",")
        stack = []
        for val in preorder:
            stack.append(val)
            while self.twoConsecutive(stack):
                stack = stack[:-3]
                stack.append("#")

        return stack == ["#"]

    def twoConsecutive(self, stack):
        if len(stack) < 3:
            return False
        return stack[-1] == stack[-2] == "#" and stack[-3] != "#"


class Solution_2(object):
    """
    Refer to:
    https://leetcode.com/discuss/83824/7-lines-easy-java-solution
    In a binary tree, if we consider null as leaves, then
        1. all non-null node provides 2 outdegree and 1 indegree(except root).
        2. all null node provides 0 outdegree and 1 indegree.

    Record diff = outdegree - indegree. When the next node comes:
    Decrease diff by 1, because the node provides an indegree.
    If the node is not null, increase diff by 2, because it provides two out degrees.

    diff should never be negative and diff will be zero when finished.
    """
    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        diff = 1
        for val in preorder:
            diff -= 1
            if diff < 0:
                return False
            if val != "#":
                diff += 2
        return diff == 0

"""
""
"#,#"
"1,#"
"1,#,#"
"#,#,#"
"1,#,#,#,#"
"9,#,#,1"
"9,3,4,#,#,1,#,#,2,#,6,#,#"
"""
