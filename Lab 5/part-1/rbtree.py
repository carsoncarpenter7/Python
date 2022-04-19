#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-11
# carson.carpenter7@csu.fullerton.edu
#

""" Class for rbtreedemo and rbtreenode"""
from rbtreenode import *

#black = white
#red = red

class RBTree:
    """ Creating a Red Black (white) Tree """
    def __init__(self):
        self._nil = RBTreeNode('nil', None, None, None, 'white')
        self._nil.parent = self._nil
        self._nil.left = self._nil
        self._nil.right = self._nil
        self._root = self._nil
        self._color = self._nil

    def left_rotate(self, x):
        """ Tree Balancing """
        y = x.right
        x.right = y.left
        if y.left != self._nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self._nil:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """ A mirror image of left_rotate"""
        y = x.left
        x.left = y.right
        if y.right != self._nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self._nil:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        """ Insert into node if key matches then set to red if it is red """
        z = RBTreeNode(key, self._nil, self._nil, self._nil, 'white')
        y = self._nil
        x = self._root
        while x != self._nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self._nil:
            self._root = z
        elif y.key > z.key:
            y.left = z
        else:
            y.right = z

        z.left = self._nil
        z.right = self._nil
        z.color = 'red'
        self.insert_fixup(z)

    def insert_fixup(self, z):
        """ Inserting and balancing tree nodes """
        while z.parent.color == 'red':
            if z.parent == z.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'white'
                    y.color = 'white'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'white'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
            # Same as above but reflected
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color == 'white'
                    y.color = 'white'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'white'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self._root.color = 'white'

    def _transplant(self, u, v):
        """ Replacing a subtree with another one """
        if u.parent == self._nil:
            self._root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != self._nil:
            v.parent = u.parent

    def _predecessor(self, x):
        """ Return the Successor Node """
        if x.right != self._nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self._nil and x == y.right:
            x = y
            y = y.parent
        return y

    def maximum(self, x):
        """ Gets Node with highest value """
        while x.right != self._nil:
            x = x.right
        return x

    def minimum(self, x):
        """ Gets Node with smallest value """
        while x.left != self._nil:
            x = x.left
        return x

    def _delete(self, z):
        """ Deletes a TreeNode Object from Tree() with the given key """
        y = z
        original_color = y.color
        if z.left == self._nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self._nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if original_color == 'white':
            self.delete_fixup(x)
            return (1)

    # def _delete(self, z):
    #     """ Deletes a TreeNode Object from Tree() with the given key """
    #     if z.left == self._nil or z.right == self._nil:
    #         y = z
    #     else:
    #         # Can get away with successor or predecessor
    #         y = self._predecessor(z)
    #     if y.left != self._nil:
    #         x = y.left
    #     else:
    #         x = y.right
    #     #print('x: {}'.format(x))
    #
    #     if x != self._nil:
    #         x.parent = y.parent
    #
    #     if y.parent == self._nil:
    #         self._root = x
    #     else:
    #         if y == y.parent.left:
    #             y.parent.left = x
    #         else:
    #             y.parent.right = x
    #     if y != z:
    #         #print('y != z')
    #         z.key = y.key
    #         # copy all of y into z
    #     if y.color == "white":
    #         self.delete_fixup(x)


    def delete_fixup(self, x): # done
        """ Deleting Nodes and set color """
        while x != self._root and x.color == 'white':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'white'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'white' and w.right.color == 'white':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'white':
                        w.left.color = 'white'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'white'
                    w.right.color = 'white'
                    self.left_rotate(x.parent)
                    x = self._root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'white'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 'white' and w.right.color == 'white':
                    w.color = 'red'
                    x = x.parent
                else: #last
                    if w.left.color == 'white':
                        w.right.color = 'white'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.color
                    w.color = x.parent.color
                    x.parent.color = 'white'
                    w.right.color = 'white'
                    self.left_rotate(x.parent)      #might be right_rotate
                    x = self._root
        x.color = 'white'



    def _search(self, x, k):
        """ Returns a TreeNode object with the given key in the tree object (secret)"""
        if x == self._nil or k == x.key:
            return x
        if k < x.key:
            return self._search(x.left, k)
        else:
            return self._search(x.right, k)

    def search(self, k):
        """ Returns a TreeNode with the given key(k) starting from self._root"""
        return self._search(self._root, k)

    def remove(self, k):
        """ Remove/Delete function """
        z = self.search(k)
        self._delete(z)
        return(1)
