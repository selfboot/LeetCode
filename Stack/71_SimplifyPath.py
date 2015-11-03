#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return "/"

        stack = []
        path_str = ""
        index = 0
        while index < len(path):
            char = path[index]
            if char == "/":
                # './' respresent current directory
                if path_str == "." or path_str == "":
                    path_str = ""

                # '../' represent parent directory
                elif path_str == "..":
                    if stack:
                        stack.pop()
                    path_str = ""

                # 'path/': push path to stack
                else:
                    stack.append(path_str)
                    path_str = ""
            else:
                path_str += char
            index += 1

        # Append the last path
        if path_str == "..":
            if stack:
                stack.pop()
        elif path_str == "." or path_str == "":
            pass
        else:
            stack.append(path_str)
        return "/" + "/".join(stack)

"""
""
"/"
"/.."
"/home.as//"
"/home.as"
"/a/./b/../../c/"
"/a/./b/../../c/../"
"/a/./b/c/../.."
"/..."
"""
