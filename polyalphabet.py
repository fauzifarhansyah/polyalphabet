def polyalphabetic_zigzag(text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def main():
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    key = input("Masukkan kunci enkripsi: ")
    encrypted_text = polyalphabetic_zigzag(plaintext, key)
    
    print("Teks terenkripsi:", encrypted_text)

if __name__ == "__main__":
    main()