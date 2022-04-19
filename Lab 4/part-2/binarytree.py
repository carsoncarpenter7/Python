#!/usr/bin/env python3
#binarytree.py
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-07
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program that outputs a binary tree """

import random
import sys
from tree import *


def list_to_string(lst):
    """ Function for formatting node """
    sim = ''
    num = 0
    for i in lst:
        number = str(i)
        lnum = number.count('null')
        if lnum != 0:
            numb = number.find('null') + 4
            numbe = number.find('nul', numb + 1) + 4
            end = len(number)
            num += 1
            different = number[0:numb] + str(num) + number[numb:numbe] + str(num)
            if lnum == 2:
                number = different + number[numbe:end]
            elif lnum == 4:
                num += 1
                nums = str(num)
                numberr = number.find('null', numbe + 1) + 4
                numberrr = number.find('null', numberr + 1) + 4
                number = different + number[numbe:numberr] + nums + number[numberr:numberrr] + nums + number[numberrr:end]
        sim += number
    return sim

def _writetree(tree, file_name):
    """" Write function """
    file_name.write('diagraph BST{\n')
    file_name.write('\tnode [fontsize=11 fontname="Helvetixca"];\n')
    file_name.write('\tedge [arrowhead=vee];\n')
    lst = []
    tree.preorder_traversal(tree.root, lst)
    file_name.write(list_to_string(lst))
    file_name.write('}')

    
def main():
    if len(sys.argv) < 2:
        print('Please provide the number of numbers to enter.')
        sys.exit(1)
    s = int(sys.argv[1])
    parts = int(s/3)
    t = Tree()
    r = list(range(1, s+1))

    print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

    random.shuffle(r)

    for i in r:
        print('inserted {}'.format(i))
        t.insert(i)

        f = open('a.dot', 'w')
        _writetree(t, f)
        f.flush()
        f.close()
        random.shuffle(r)

    for n in range(1, 3):
        m = r[(n-1) * parts : (n * parts)]
        print(len(m))
        for i in m:
            print('removed {}'.format(i))
            v = t.remove(i)
            if v:
                print('\tcompleted.')
            else:
                print('\terror.')
        c = chr(n + 97)
        filename = str(c) + '.dot'
        f = open(filename, 'w')
        _writetree(t, f)
        f.flush()
        f.close()

if __name__ == '__main__':
    main()
