#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        l_child = root.left
        r_child = root.right
        if not l_child and not r_child:
            return True

        # Check the root's childrens.
        if l_child and r_child and l_child.val == r_child.val:
            return self.is_symmetric(l_child, r_child)
        return False

    # Find out whether two nodes and their childrens
    # are symmetric around the center
    def is_symmetric(self, left_node, right_node):
        lnode_lchild = left_node.left
        lnode_rchild = left_node.right
        rnode_lchild = right_node.left
        rnode_rchild = right_node.right

        # Figure out whether the left child of left node and
        # the right child of right node is symmetric, if not, return False
        if ((lnode_lchild and rnode_rchild and
                lnode_lchild.val == rnode_rchild.val
                and self.is_symmetric(lnode_lchild, rnode_rchild))
                or (not lnode_lchild and not rnode_rchild)):
            pass
        else:
            return False

        # Figure out whether the right child of left node and
        # the left child of right node is symmetric, if not, return False
        if ((lnode_rchild and rnode_lchild and
                lnode_rchild.val == rnode_lchild.val
                and self.is_symmetric(lnode_rchild, rnode_lchild))
                or (not lnode_rchild and not rnode_lchild)):
            pass
        else:
            return False

        # Both two situations are symmetric, then return True
        return True

"""
[]
[1]
[1,2,3]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
"""
