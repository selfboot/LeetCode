#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# The leetcode way
class Codec:
    def serialize(self, root):
        data = []
        node_queue = [root]
        start = 0
        while start < len(node_queue):
            node = node_queue[start]
            start += 1
            if node:
                data.append(str(node.val))
                node_queue.append(node.left)
                node_queue.append(node.right)
            else:
                data.append("null")
        # Remove the tail null node.
        while data and data[-1] == "null":
            del data[-1]
        return ",".join(data)

    def deserialize(self, data):
        if not data:
            return None

        # Get all the nodes.
        data_list = data.split(",")
        length = len(data_list)
        node_list = [0] * length
        for i in range(length):
            if data_list[i] == "null":
                node_list[i] = None
            else:
                node_list[i] = TreeNode(int(data_list[i]))

        # Build the tree.
        offset = 1
        cur_pos = 0
        while offset < length:
            if node_list[cur_pos]:
                node_list[cur_pos].left = node_list[offset]
                offset += 1
                if offset < length:
                    node_list[cur_pos].right = node_list[offset]
                    offset += 1
                else:
                    break
            else:
                pass
            cur_pos += 1

        return node_list[0]


class Codec_2:
    # Refer to: Recursive preorder, Python and C++, O(n)
    # https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
    def serialize(self, root):
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('#')

        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        vals = iter(data.split())
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))(codec.deserialize("1,null,3,4,5"))

"""
[]
[1,2,null,3,4]
[1,2,3,null,4,null,5,null,6,7]
"""
