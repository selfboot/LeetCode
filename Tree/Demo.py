#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-21 09:49:20


def inorderTraversal(self, root):
    tree_stack = []
    inorder_tra = []
    while root or tree_stack:
        # Go along the left child
        if root:
            tree_stack.append(root)
            root = root.left
        # Meet a left, go back to the parent node
        else:
            node = tree_stack.pop()
            inorder_tra.append(node.val)
            root = node.right

    return inorder_tra
