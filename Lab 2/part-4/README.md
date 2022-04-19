# CPSC 223p
##  Vigenère Cipher


Write a program named `vigenere.py` which implements the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

The Vigenère cipher is a polyalphabetic substitution cipher. It is a variation of Caesar's cipher where the alphabet is shifted by a fixed number of letters. For example, if the alphabet is shifted by eight, then the unshifted alphabet (first line) will map the following letters (second line):
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
IJKLMNOPQRSTUVWXYZABCDEFGH
```

The Vigenère cipher uses 26 alphabets that are each progressive shifted from 0 to 26. The code word provides an index into which one of the shifted alphabets will be used to cipher each letter of the clear text message into cipher text. For example, the clear text is "The eagle has landed" and the code word is "lime".
```
The eagle has landed.
limelimelimelimelimel
```

The first letter 'T' is ciphered using the alphabet that matches 'l', which is a shift of 12 letters; 'l' is the twelfth letter of the alphabet. The next letter 'h' matches 'i' which is a shift of 9 letters, etc.

The cleartext `The eagle has landed.` when ciphered using the code word `lime` is `Epq$pispp(ted(xeylqh9`.

Write a program named `vigenere.py` that can cipher and decipher using the Vigenère cipher. By using command line arguments, determine if the program shall cipher a cleartext or decipher a ciphertext.
* If there are no arguments or too few, print out instructions and exit gracefully.
* To cipher text, the first argument is `cipher`, the second argument is the codeword, and the third argument is the string to cipher.
* To decipher text, the first argument is `decipher`, the second argument is the codeword, and the third argument is the string to decipher.

## Example Output
'''
$ ./vigenere.py 
Please provide a command, cipher or decipher, a codeword, and a message.
$ ./vigenere.py encrypt lime 'The eagle has landed.'
Command, encrypt, was not understood.
$ ./vigenere.py cipher lime 'The eagle has landed.'
Epq$pispp(ted(xeylqh9
$ ./vigenere.py decipher lime 'Epq$pispp(ted(xeylqh9'
The eagle has landed.
'''

To pass the message to the program, use single quotes rather than double quotes because if the ciphertext has special characters most shells will ignore the special characters when you wrap your input in single quotes.