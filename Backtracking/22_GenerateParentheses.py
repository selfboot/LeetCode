#! /usr/bin/env python
# -*- coding: utf-8 -*-


def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    # node = [leftchild, rightchild, count"(", count")", current str]
    if not n:
        return [""]
    solution = []
    root = [None, None, 1, 0, "("]
    self.generate_child_tree(root, n, solution)
    return solution


def generate_child_tree(self, node, n, solution):
    # the node is the leave and the str is what we want
    if node[2] == node[3] == n:
        node[0] = None
        node[1] = None
        solution.append(node[4])

    # the node have both left and right child
    elif node[2] > node[3] and node[2] < n:
        left_child = [None, None, node[2] + 1, node[3], node[4] + "("]
        right_child = [None, None, node[2], node[3] + 1, node[4] + ")"]
        node[0] = left_child
        node[1] = right_child
        self.generate_child_tree(left_child, n, solution)
        self.generate_child_tree(right_child, n, solution)

    # the node have only left child
    elif node[2] == node[3] and node[2] < n:
        left_child = [None, None, node[2] + 1, node[3], node[4] + "("]
        node[0] = left_child
        self.generate_child_tree(left_child, n, solution)

    # the node have only left child
    else:
        right_child = [None, None, node[2], node[3] + 1, node[4] + ")"]
        node[1] = right_child
        self.generate_child_tree(right_child, n, solution)

"""
0
1
3
5
"""
