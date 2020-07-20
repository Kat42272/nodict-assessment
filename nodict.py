#!/usr/bin/env python3
"""
Implementation of the NoDict assignment and Tests
"""

__author__ = 'Kathryn Anderson with the help of Kano'


class Node:
    def __init__(self, key, value=None):
        """ This initializes the class Node 
        and defines the instance variables """
        self.hash = hash(key)
        self.key = key
        self.value = value
        return
        

    def __repr__(self):
        """ This creates the object """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """ This returns a comparison of nodes by key and hash """
        return self.hash == other.hash and self.key == other.key
    


class NoDict:
    def __init__(self, num_buckets=10):
        """ This initializes the class NoDict 
        and defines the instance variables """
        self.size = num_buckets
        self.buckets = [[] for i in range(num_buckets)]

    def __repr__(self):
        """ Returns a string that displays the contents of NoDict """
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, 
            bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """ This adds a node NoDict """
        new_node = Node(key, value)
        bucket_index = self.buckets[new_node.hash % self.size]
        for node in bucket_index:
            if node == new_node:
                bucket_index.remove(node)
                break
        bucket_index.append(new_node)

    def get(self, key):
        """ This looks for a Node key and returns
        the value of that key. If no key an error is raised """
        find_node_key = Node(key)
        current_bucket = self.buckets[find_node_key.hash % self.size]

        for node in current_bucket:
            if node == find_node_key:
                return node.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """ This gets and returns the key item and it's value """
        return self.get(key)

    def __setitem__(self, key, value):
        """ This returns and sets the key item and it's value """
        return self.add(key, value)