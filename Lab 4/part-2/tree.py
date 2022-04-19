#!/usr/bin/env python3
#tree.py
from treenode import *

class Tree:
    """A binary tree class."""
    __direction__ = {'_root'}

    def __init__(self):
        """ Default """
        self._root = None

    # The 'root' property
    @property
    def root(self):
        """ Root getter """
        return self._root

    @root.setter
    def root(self, node):
        """ Root setter """
        self._root = node


    def isEmpty(self):
        """ Root is empty setter """
        return self.root == None

    def insert(self, key):
        """ Inserting into Tree """
        location = self.root
        top = None
        while location != None:
            top = location
            if location.number > key:
                location = location.left
            else:
                location = location.right
        new_node = TreeNode(top, key)
        if top == None:
            self.root = new_node
        elif top.number > key:
            top.left = new_node
        else:
            top.right = new_node

    def _search(self, node, key):
        """ Find key """
        while node != None and node.number != key:
            if key > node.number:
                node = node.right
            else:
                node = node.left
        return node

    def _localMin(self, start):
        """ Find Min """
        node = start
        while node.left != None:
            node = node.left
        return node

    def _localMax(self, start):
        """ Find max """
        node = start
        while node.right != None:
            node = node.right
        return node

    def key(self, key):
        """ Return root with key """
        return self._search(self.root, key)

    def remove(self, key):
        """ Remove node """
        node = self.key(key)
        if node != None:
            self.no_node(node)
            return True
        else:
            return False

    def minimum(self):
        """ Set Min """
        return self._localMin(self.root)

    def maximum(self):
        """ Set Max """
        return self._localMax(self.root)

    def remove(self, key):
        """ Remove node """
        node = self.key(key)
        if node != None:
            self.no_node(node)
            return True
        else:
            return False

    def _transplant(self, x, y):
        """ Balance Tree """
        if x.top == None:
            self.root = y
        elif x.isleft():
            x.top.left = y
        else:
            x.top.right = y
        if y != None:
            y.top = x.top

    def no_node(self, node):
        """ Balance Tree/ Delete Node """
        if node.left == None:
            self._transplant(node, node.right)
        elif node.right == None:
            self._transplant(node, node.left)
        else:
            successor = self._localMin(node.right)
            if successor.top != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.top = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.top = successor
        del node

    def preorder_traversal(self, start, lst):
        """ Traverse Tree Nodes """
        if start is None:
            lst.append(str(start))
            if start.left is None:
                self.preorder_traversal(start.left, lst)
            if start.right is None:
                self.preorder_traversal(start.right, lst)
