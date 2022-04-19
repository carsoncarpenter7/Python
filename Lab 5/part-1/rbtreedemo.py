#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-11
# carson.carpenter7@csu.fullerton.edu
#

"""
This is my program that outputs a binary tree that is red or black"""

import random
import sys
from rbtree import *

# converting dot files to pdf:
# dot -Tpdf a.dot -o graph1.pdf or dot -Tpng a.dot > a.png
# compile with: ./rbtreedemo.py  15


def writeRBTree(t, out):
  def _writeNull(n, nullcount, out):
    out.write('\tnull' + str(nullcount) + ' [shape=point];\n')
    out.write('\t' + str(n.key) + ' -> null' + str(nullcount) + ';\n')

  def _writeHelper(n, out, nullcount):
    n.color = 'red'                                          #print out details on node afetr visiting; like "[style="filled" fillcolor="red"]"
    if n.left != t._nil:
      out.write( '\t' + str(n.key) + f' [style="filled" fillcolor="{n.color}"]\n')
      out.write( '\t' + str(n.key) + ' -> ' + str(n.left.key) + ';\n')
      nullcount = _writeHelper( n.left, out, nullcount)
    else:
      nullcount += 1
      _writeNull(n, nullcount, out)
      n.color = 'white'
      if n.right != t._nil:
          out.write( '\t' + str(n.key) + ' -> ' + str(n.right.key) + ';\n')
          nullcount = _writeHelper(n.right, out, nullcount)
      else:
          nullcount += 1
          _writeNull(n, nullcount, out)
          return nullcount

  out.write('digraph BST{\n')
  out.write('\tnode [fontname="Helvetica"];\n')
  if t._root == t._nil:
    out.write('\n')
  elif t._root.right == t._nil and t._root.left == t._nil:
    out.write('\t' + str(t._root.key) + ';\n')
  else:
    _nullCount = 0
    _writeHelper( t._root, out, _nullCount )                                       #null count = global variable but really just a parameter
  out.write('}\n')


def main():
    if len(sys.argv) < 2:
        print('Please provide the number of keys to enter.')
        sys.exit(1)

    s = int(sys.argv[1])
    parts = int(s/3)
    t = RBTree()
    r = list(range(1, s+1))

    print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

    random.shuffle(r)

    for i in r:
        print('inserted {}'.format(i))
        t.insert(i)

    f = open('a.dot', 'w')
    writeRBTree(t, f)
    f.flush()
    f.close()
    random.shuffle(r)

    for n in range(1, 3):
        m = r[(n-1) * parts:(n * parts)]
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
        writeRBTree(t, f)
        f.flush()
        f.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
