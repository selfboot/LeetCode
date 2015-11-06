#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthes_stack = []
        match_rule = {")": "(", "]": "[", "}": "{"}
        for symble in s:
            if symble == "(" or symble == "[" or symble == "{":
                parenthes_stack.append(symble)

            else:
                # Check if stack top matches the current ), ] or }.
                if (parenthes_stack and
                        parenthes_stack[-1] == match_rule[symble]):
                    parenthes_stack.pop()
                else:
                    return False
        # Have some symbles that is not matched.
        if parenthes_stack:
            return False

        return True

"""
""
"["
"()()()()[]"
"()((()){})"
"""
