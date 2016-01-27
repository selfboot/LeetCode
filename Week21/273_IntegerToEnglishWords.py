#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def numberToWords(self, num):
        self.words_conv = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
            40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
            90: "Ninety", 100: "Hundred", 1000: "Thousand", 1000000: "Million",
            1000000000: "Billion"
        }

        if num <= 20:
            return self.words_conv[num]
        elif num < 999:
            return self.convert_three(num)
        else:
            bill, bill_str = num / 1000000000, ""
            mill, mill_str = num % 1000000000 / 1000000, ""
            thou, thou_str = num % 1000000 / 1000, ""
            hund, hund_str = num % 1000, ""
            if bill:
                bill_str = self.convert_three(bill) + " Billion "
            if mill:
                mill_str = self.convert_three(mill) + " Million "
            if thou:
                thou_str = self.convert_three(thou) + " Thousand "
            if hund:
                hund_str = self.convert_three(hund)
            str = bill_str + mill_str + thou_str + hund_str
            # Erase the tailing space, when num = 1000...
            while str[-1] == " ":
                str = str[:-1]
            return str

    def convert_three(self, num):
        # assert(num < 1000)
        if num < 100:
            return self.convert_two(num)
        else:
            str = self.words_conv[num/100] + " " + self.words_conv[100]
            other = self.convert_two(num % 100)
            if other:
                str = str + " " + other
            return str

    def convert_two(self, num):
        # assert(num < 100)
        if not num:
            return ""
        if num <= 20:
            return self.words_conv[num]
        else:
            if num % 10 != 0:
                return (
                    self.words_conv[num/10*10] + " " +
                    self.words_conv[num % 10])
            else:
                return self.words_conv[num/10*10]

"""
0
9
10
14
20
22
99
100
101
999
1000
1001
1999
9999
1000010
1010010
1110010
1110001
2001000000
2000001000
2111111001
2147483647
"""
