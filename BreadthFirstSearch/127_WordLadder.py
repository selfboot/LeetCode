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
                one_distance = 0
                for i in range(cur_len):
                    if cur_word[i] != endWord[i]:
                        if one_distance == 1:
                            one_distance = 0
                            break
                        one_distance += 1
                if one_distance == 1:
                    return length + 1

                # Get the next level
                # When I put "abc...xyz" in the out loop, it just exceeded.
                for i in range(cur_len):
                    pre_word = cur_word[:i]
                    post_word = cur_word[i+1:]
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        next_word = pre_word + j + post_word
                        if (next_word not in visited_word and
                                next_word in wordList):
                            next_level.append(next_word)
                            visited_word[next_word] = 1
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
""" Test Case
if __name__ == '__main__':
    sol = Solution()
    print sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print sol.ladderLength("hit", "cog", ["hot", "dot", "doh", "lot", "loh"])
    print sol.ladderLength(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "hig", "hog"])
    print sol.ladderLength(
        "cet",
        "ism",
        ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay",
         "sip", "kay", "per", "val", "mes", "ohs", "now", "boa", "cet", "pal",
         "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit",
         "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row",
         "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has",
         "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu",
         "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
         "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
         "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan",
         "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye", "lye",
         "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot",
         "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
         "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm",
         "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
         "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag",
         "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
         "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his",
         "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
         "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib",
         "rub", "ere", "dig", "era", "cat", "fox", "bee", "mod", "day", "apr",
         "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
         "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx",
         "jog", "nun", "par", "wan", "fey", "bus", "oak", "bad", "ats", "set",
         "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
         "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap",
         "lop", "may", "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky",
         "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo",
         "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
         "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep",
         "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed",
         "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum",
         "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
         "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen",
         "oaf", "mix", "hep", "fur", "ada", "bin", "nil", "mia", "ewe", "hit",
         "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
         "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
         "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui",
         "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo",
         "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas",
         "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
         "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit",
         "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
         "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid",
         "pun", "ton", "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil",
         "jig", "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig",
         "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty",
         "lap", "two", "ins", "con", "ant", "net", "tux", "ode", "stu", "mug",
         "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
         "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
         "err", "him", "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego",
         "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big",
         "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot",
         "ora", "tia", "kip", "han", "met", "hut", "she", "sac", "fed", "goo",
         "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid",
         "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref",
         "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
         "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid",
         "mai", "sup", "jay", "hob", "mow", "jot", "are", "pol", "arc", "lax",
         "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe",
         "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"]
    )
"""
