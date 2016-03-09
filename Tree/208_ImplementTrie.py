#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/49529/my-python-solution


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Inserts a word into the trie.
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
        cur_node.is_word = True

    def search(self, word):
        # Returns if the word is in the trie.
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        return cur_node.is_word

    def startsWith(self, prefix):
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        cur_node = self.root
        for ch in prefix:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        return True

"""
if __name__ == '__main__':
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")
    trie.insert("rental")
    print trie.search("apps")
    print trie.search("app")
    print trie.search("ad")
"""
