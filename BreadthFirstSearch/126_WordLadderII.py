#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        if beginWord == endWord:
            return [[beginWord]]
        cur_level = [beginWord]
        next_level = []
        visited_word = {}
        visited_word[beginWord] = 1

        # BFS: find whether there are shortest transformation sequence(s)
        find_shortest = False
        self.pre_word_list = {}
        while cur_level:
            if find_shortest:
                break
            for cur_word in cur_level:
                cur_len = len(cur_word)
                # Get the next level
                # When I put "abc...xyz" in the out loop, it just exceeded.
                for i in range(cur_len):
                    pre_word = cur_word[:i]
                    post_word = cur_word[i+1:]
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        next_word = pre_word + j + post_word
                        # Just find one shorttest transformation sequence
                        if next_word == endWord:
                            find_shortest = True
                        else:
                            pass
                        if (next_word not in visited_word and
                                next_word in wordlist or next_word == endWord):
                            if next_word not in next_level:
                                next_level.append(next_word)
                            else:
                                pass

                            if next_word not in self.pre_word_list:
                                self.pre_word_list[next_word] = [cur_word]
                            else:
                                self.pre_word_list[next_word].append(cur_word)
                        else:
                            pass
            for w in next_level:
                visited_word[w] = 1
            # Scan the next level then
            cur_level = next_level
            next_level = []
        if find_shortest:
            self.results = []
            self.dfs_sequences(beginWord, endWord, [endWord])
            return self.results
        else:
            return []

    """
    Build the path according to the pre_word_list
    """
    def dfs_sequences(self, beginWord, endWord, path):
        if beginWord == endWord:
            self.results.append(list(path[-1::-1]))
        elif endWord in self.pre_word_list:
            for pre_w in self.pre_word_list[endWord]:
                path.append(pre_w)
                self.dfs_sequences(beginWord, pre_w, path)
                path.pop()
        else:
            pass
        return

"""
if __name__ == '__main__':
    sol = Solution()

    print sol.findLadders("hit", "hhh", ["hot", "dot", "dog", "lot", "log"])
    print sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print sol.findLadders(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "hog"])

    print sol.findLadders(
        "cet", "ism",
        ['cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'get',
         'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm'])
"""
