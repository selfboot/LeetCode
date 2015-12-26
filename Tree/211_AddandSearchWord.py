#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
import collections


class WordDictionary(object):
    # One faster, easy understand way
    # Refer to:
    # https://leetcode.com/discuss/69963/python-168ms-beat-100%25-solution
    def __init__(self):
        self.words_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.words_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        for w in self.words_dict[len(word)]:
            is_match = True
            for i, ch in enumerate(word):
                if ch != "." and ch != w[i]:
                    is_match = False
                    break
            if is_match:
                return True
        return False


class TrieNode():
    # Refer to: 208. Implement Trie
    def __init__(self):
        self.is_word = False
        self.childrens = {}


class WordDictionary_Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.childrens:
                cur_node.childrens[ch] = TrieNode()
            cur_node = cur_node.childrens[ch]
        cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        """
        return self._dfs_searh(word, self.root)

    # Depth First Search the trie tree.
    def _dfs_searh(self, word, cur_node):
        if not word and cur_node.is_word:
            return True
        word_len = len(word)
        for i in range(word_len):
            ch = word[i]
            if ch == ".":
                for child_ch in cur_node.childrens:
                    if self._dfs_searh(word[i+1:],
                                       cur_node.childrens[child_ch]):
                        return True
                return False
            else:
                if ch not in cur_node.childrens:
                    return False
                else:
                    cur_node = cur_node.childrens[ch]
        if cur_node.is_word:
            return True
        else:
            return False

"""
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print wordDictionary.search("xad")
    print wordDictionary.search(".a")
    print wordDictionary.search(".ad")
    print wordDictionary.search("b.")
    print wordDictionary.search(".")
"""
