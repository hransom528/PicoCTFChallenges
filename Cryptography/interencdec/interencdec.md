# interencdec
### Category: Cryptography
### Harris A. Ransom

## Challenge
Can you get the real meaning from this file?
File: enc_flag

## Solution
Steps to decode (using [CyberChef](https://cyberchef.org)):
- Convert from Base64: b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ=='
- Remove b' ' (this just signals it's a bytestring): d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ==
- Convert from Base64: wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}
- ROT13 Bruteforce (n = 19): picoCTF{caesar_d3cr9pt3d_ea60e00b}

**Flag:** picoCTF{caesar_d3cr9pt3d_ea60e00b}