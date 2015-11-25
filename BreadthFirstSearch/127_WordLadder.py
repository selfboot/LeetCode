#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Breadth First Search
        When build the adjacency tree, skip the visited word
        """
        if beginWord == endWord:
            return 1
        cur_level = [beginWord]
        next_level = []
        visited_word = {}
        visited_word[beginWord] = 1
        length = 0
        while cur_level:
            length += 1
            for cur_word in cur_level:
                cur_len = len(cur_word)
                # Get the next level
                # When I put "abc...xyz" in the out loop, it just exceeded.
                for i in range(cur_len):
                    pre_word = cur_word[:i]
                    post_word = cur_word[i+1:]
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        next_word = pre_word + j + post_word
                        # Find the endWord
                        if next_word == endWord:
                            return length + 1
                        elif (next_word not in visited_word and
                                next_word in wordList):
                            visited_word[next_word] = 1
                            next_level.append(next_word)
                        else:
                            pass

            # Scan the next level then
            cur_level = next_level
            next_level = []
        return 0

    """ disapproved, when wordList growth bigger, it may be called too many times
    def is_one_distance(self, word_1, word_2):
        # alert(len(word_1) == len(word_2))
        word_l = len(word_1)
        one_distance = False
        for i in range(word_l):
            if word_1[i] != word_2[i]:
                if not one_distance:
                    one_distance = True
                else:
                    return False

        return one_distance
    """
"""
if __name__ == '__main__':
    sol = Solution()
    print sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print sol.ladderLength("hit", "cog", ["hot", "dot", "doh", "lot", "loh"])
    print sol.ladderLength(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "hig", "hog"])

    print sol.ladderLength(
        "cet", "ism",
        ['cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'get',
         'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm'])
"""
