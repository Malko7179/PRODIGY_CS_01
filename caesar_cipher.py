def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    if mode == "encrypt":
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    elif mode == "decrypt":
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
