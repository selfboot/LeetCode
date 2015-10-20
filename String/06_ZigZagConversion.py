class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s

        len_s = len(s)
        zigzag_list = []
        magic_number = 2 * numRows - 2

        for row in range(numRows):
            index = row
            while index < len_s:
                zigzag_list.append(s[index])
                if row != 0 and row != numRows - 1:
                    next_num = magic_number + index - 2 * row
                    if next_num < len_s:
                        zigzag_list.append(s[next_num])
                index += magic_number

        return "".join(zigzag_list)

"""
""
1
"ABC"
1
"PAYPALISHIRING"
5
"""
