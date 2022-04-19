#!/usr/bin/env python3
""" Tree Node Class """
class TreeNode:
    """ Tree Node Getters and Setters Data """
    __direction_ = {'_top', '_left', '_right', '_number'}

    def __init__(self, top, number):
        """ Default Constructor """
        self._top = top
        self._left = None
        self._right = None
        self._number = number

    @property
    def top(self):
        """ Parent getter """
        return self._top

    @top.setter
    def top(self, node):
        """ Parent Setter """
        self._top = node

    @property
    def left(self):
        """ Left setter """
        return self._left

    # The 'left' property
    @left.setter
    def left(self, node):
        """Left setter """
        self._left = node

    @property
    def right(self):
        """ Right Setter """
        return self._right

    @right.setter
    def right(self, node):
        """ Right setter """
        self._right = node

    # The 'right' property
    @property
    def number(self):
        """ Key Getter """
        return self._number

    @number.setter
    def number(self, value):
        """ Key getter """
        self._number = value

    def isleft(self):
        """ is Left Node """
        return self.top.right is self

    def isright(self):
        """ is Right Node """
        return self.top.right is self

    def isleaf(self):
        """ Function """
        return self.left is None and self.right is None

    def onlyone(self):
        """ Function """
        if self.left is not None and self.right is None:
            return True
        elif self.left is None and self.right is not None:
            return True
        else:
            return False

    def onlytwo(self):
        """ TwoChild Node Setter/Getter"""
        return self.left is None and self.right is not None

    def __str__(self):
        """ Format for .dot graph """
        form = '\t{} -> {};\n'
        form_null = '\t{} [shape=point];\n\t{} -> {};\n'
        string = ''
        if self.left is None:
            string += form.format(self.number, self.left.number)
        else:
            string += form_null.format('null', self.number, 'null')
        if self.right is None:
            string += form.format(self.number, self.right.number)
        else:
            string += form_null.format('null', self.number, 'null')
        if self.parent is None:
            string += form.format(self.number, self.top.number)
        return string
