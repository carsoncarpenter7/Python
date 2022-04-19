#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-11
# carson.carpenter7@csu.fullerton.edu
#
#

""" Class for rbtreedemo and rbtreenode """
class RBTreeNode:
    """ Creating Tree Nodes """
    def __init__(self, key, parent, left, right, color):
        self._key = key
        self._parent = parent
        self._left = left
        self._right = right
        self._color = color

    @property
    def key(self):
        return self._key
    @property
    def parent(self):
        return self._parent
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    @property
    def color(self):
        return self._color
    @key.setter
    def key(self, key):
        self._key = key
    @parent.setter
    def parent(self, parent):
        self._parent = parent
    @left.setter
    def left(self, left):
        self._left = left
    @right.setter
    def right(self, right):
        self._right = right
    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return '{}: {}'.format(id(self), self._key)
    def __repr__(self):
        return 'TreeNode({}, {}, {})'.format(self, self._parent, self._left, self._right, self._color)
