def CaesarEncrypt(plaintext, key):
    ans = ""
    for letter in plaintext:
        if letter >= 'a' and letter <= 'z':
            ans += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        elif letter >= 'A' and letter <= 'Z':
            ans += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
        else:
            ans += letter
    return ans

def CaesarDecrypt(cipher, key):
    ans = ""
    for letter in cipher:
        if letter >= 'a' and letter <= 'z':
            ans += chr(ord(letter) - key) if ord(letter) - key >= ord('a') else chr(ord(letter) - key + ord('a')) 
        elif letter >= 'A' and letter <= 'Z':
            ans += chr(ord(letter) - key) if ord(letter) - key >= ord('A') else chr(ord(letter) - key + ord('A'))
        else:
            ans += letter
    return ans
text = input()
k = int(input())
print(CaesarEncrypt(text, k))
print(CaesarDecrypt(CaesarEncrypt(text, k), k))
