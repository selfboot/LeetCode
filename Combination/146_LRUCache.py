#! /usr/bin/env python
# -*- coding: utf-8 -*-


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.doubleLinkedList = DoubleLinkedList()
        self.len = 0

    def get(self, key):
        # Get operator will also update the linked list(Don't forget)
        if key in self.cache:
            node = self.cache[key]
            self.doubleLinkedList.delete(node)
            self.doubleLinkedList.append(node)
            return self.cache[key].value
        else:
            return -1

    def set(self, key, value):
        # update the (key,value) pair in both hash and linked list.
        if key in self.cache:
            node = self.cache[key]
            self.doubleLinkedList.delete(node)
            new_node = Node(key, value)
            self.doubleLinkedList.append(new_node)
            self.cache[key] = new_node

        else:
            node = Node(key, value)
            # Add the new node to cache
            if self.len < self.capacity:
                self.doubleLinkedList.append(node)
                self.cache[key] = node
                self.len += 1
            # Remove the head of linked list and append the new node
            else:
                replaced_node = self.doubleLinkedList.del_head()
                del self.cache[replaced_node.key]
                self.doubleLinkedList.append(node)
                self.cache[key] = node


class Node:
    def __init__(self, key=None, value=None, next_node=None, pre_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.pre = pre_node


# Double linked list
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

    def delete(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
        elif node == self.head:
            node.next.pre = None
            self.head = node.next
        elif node == self.tail:
            node.pre.next = None
            self.tail = node.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

    def del_head(self):
        del_head = self.head
        self.delete(self.head)
        return del_head

"""
if __name__ == '__main__':
    ca = LRUCache(2)
    ca.set(2, 1)
    print "AA", ca.get(2)
    ca.set(2, 2)
    print "BB",  ca.get(2)
    ca.set(3, 3)
    print "CC", ca.get(3)
    # what if: print "CC", ca.get(2)
    ca.set(4, 1)
    print "CC", ca.get(2)
"""
