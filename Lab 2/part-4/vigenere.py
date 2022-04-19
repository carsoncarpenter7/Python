#!/usr/bin/env python3
#
# Carson Carpenter
# 2020-10-06
#
#
""" Robinhood Trading Bot """

import pyotp
import robin_stocks as r



def main():
    """ This Program gets the keyword and user input from the terminal
    and either encrpts or decrypts the user message"""


def keyword(key_code, user_input):
    """Gets keyword and muser message"""
    pass:
    # extend_key = ""
    # index = 0
    #
    # for _ in user_input:
    #     if index >= len(key_code):
    #         index = 0
    #     extend_key += key_code[index]
    #     index += 1
    # return extend_key


def encrypt(key, user_input):
    """Takes keyword and user message and encrpyts the message using
    Vigenère Ciphe"""
    pass:
    # extend_key = keyword(key, user_input)
    # result = ""
    # size = len(user_input)
    # for i in range(size):
    #     output = (ord(user_input[i]) + 1 + LETTERS.find(extend_key[i]))
    #     if user_input[i].isupper() and output > 90:
    #         output -= 26
    #     elif user_input[i].islower() and output > 122:
    #         output -= 26
    #     result += chr(output)
    # print(result)


def decrypt(key, user_input):
    """Takes keyword and user message and decrpyts the message using
    Vigenère Ciphe"""
    pass:
    # extend_key = keyword(key, user_input)
    # result = ""
    # size = len(user_input)
    # for i in range(size):
    #     output = (ord(user_input[i]) - (1 + LETTERS.find(extend_key[i])))
    #     if user_input[i].isupper() and output < 65:
    #         output += 26
    #     elif user_input[i].islower() and output < 97:
    #         output += 26
    #     result += chr(output)
    # print(result)


if __name__ == '__main__':
    main()
    # if sys.argv[1] == 'encrypt':
    #     print("Command, " + sys.argv[1] + ", was not understood")
    # elif sys.argv[1] == 'cipher':
    #     KEY = sys.argv[2]
    #     # print(sys.argv[2])
    #     USER_INPUT = sys.argv[3]
    #     # print(sys.argv[3])
    #     encrypt(KEY, USER_INPUT)
    # else:
    #     KEY = sys.argv[2]
    #     USER_INPUT = sys.argv[3]
    #     decrypt(KEY, USER_INPUT)
