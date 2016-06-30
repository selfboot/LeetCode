#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isNumber(self, s):
        """DFA

        Details can be found here:
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_ValidNumber.png
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_StateConvert.png
        """
        s = s.strip()
        if not s:
            return False

        # DFA states change table
        DFA_states_change = {
            0: {1: 2, 2: 1, 3: 8, 4: -1},
            1: {1: 2, 2: -1, 3: 8, 4: -1},
            2: {1: 2, 2: -1, 3: 3, 4: 5},
            3: {1: 4, 2: -1, 3: -1, 4: 5},
            4: {1: 4, 2: -1, 3: -1, 4: 5},
            5: {1: 7, 2: 6, 3: -1, 4: -1},
            6: {1: 7, 2: -1, 3: -1, 4: -1},
            7: {1: 7, 2: -1, 3: -1, 4: -1},
            8: {1: 4, 2: -1, 3: -1, 4: -1}
        }
        current_state = 0
        for char in s:
            input_num = self.input_num(char)
            if not input_num:
                return False
            next_state = DFA_states_change[current_state][input_num]
            if next_state == -1:
                return False
            current_state = next_state

        if (current_state == 2 or current_state == 3 or
           current_state == 4 or current_state == 7):
            return True
        else:
            return False

    def input_num(self, char):
        if char in "0123456789":
            return 1
        elif char in "+-":
            return 2
        elif char == ".":
            return 3
        elif char == "e":
            return 4
        else:
            return 0

# True
"""
" .1"
"012"
"+12"
"-12"
"12e1"
"12e-1"
"12e+1"
"12e0"
"0e1"
"-1e1"
"1.2"
".2"
".1e1"
"+.2"
"1."
"      .1 "
"46.e3"
"""

# False
"""
""
".e1"
"+.e3"
"10e1.2"
"+-12"
"12e"
"e1"
"1e1e1"
"0xaf"
"      .1 2"
"."
"  ."
" -."
"""
