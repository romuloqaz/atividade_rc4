def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S


def PRGA(S, n):
    i = 0
    j = 0
    key = []

    while n > 0:
        n = n - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key





key = 'KAREEM'
plaintext = 'Mission Accomplished'

def preparing_key_arrays(s):
    return [ord(c) for c in s]

key = preparing_key_arrays(key)

import numpy as np

S = KSA(key)

keystream = np.array(PRGA(S, len(plaintext)))
print(keystream)

plaintext = np.array([ord(i) for i in plaintext])

cipher = keystream ^ plaintext  # xor



print (cipher.astype(np.uint8).data.hex() )  # print hex
print ([chr(c) for c in cipher])
