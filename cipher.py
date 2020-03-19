#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt(str, key):
    ciphertext = ""

    for ch in list(str):
        if 'A' <= ch <= 'Z':
            ciphertext += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            ciphertext += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            ciphertext += ch

    return ciphertext

if __name__ == '__main__':
    plaintext = input("PLEASE INPUT PLAINTEXT : ")
    key = input("PLEASE INPUT KEY : ")
    ciphertext = encrypt(plaintext, int(key))

    print("CIPHERTEXT : " + ciphertext)

    input("PLEASE PRESS ANY")
