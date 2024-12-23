def caesar_cipher_encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
