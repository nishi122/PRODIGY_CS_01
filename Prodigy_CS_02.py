from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """Encrypts an image by manipulating pixel values using a key."""
    # Open the image
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # Encrypt by applying XOR with the key
    encrypted_array = image_array ^ key
    
    # Convert back to an image and save
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    """Decrypts an image by reversing the encryption process."""
    # Open the encrypted image
    encrypted_image = Image.open(input_path)
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt by applying XOR with the same key
    decrypted_array = encrypted_array ^ key
    
    # Convert back to an image and save
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ").strip()
    
    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return
    
    input_path = input("Enter the input image file path: ").strip()
    output_path = input("Enter the output image file path: ").strip()
    key = int(input("Enter a numeric key (0-255): ").strip())
    
    if not (0 <= key <= 255):
        print("Key must be between 0 and 255!")
        return
    
    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
