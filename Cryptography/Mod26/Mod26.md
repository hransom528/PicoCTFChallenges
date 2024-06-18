# Mod 26
### Category: Cryptography
### Harris A. Ransom

## Challenge
Cryptography can be easy, do you know what ROT13 is? 
`cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}`

## Solution
This is a classic example of a **rotation cipher**, where the characters are rotated by a set number. The famous **Caesar Cipher** is an example of a rotation cipher, in which each letter is rotated forwards alphabetically by three places (e.g. A becomes D).

We are given that this is a ROT13 cipher, meaning that each character is rotated forwards by 13. So, all we have to do is rotate backwards by 13 for each character. This can be done by hand, with a Python script (or program in your language of choice), or with the website [CyberChef](https://cyberchef.org/).

**Flag:** picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}