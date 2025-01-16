from PIL import Image

def encrypt_image(image_path, key, output_path):
    """Encrypts an image using pixel manipulation."""
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure it's in RGB format
        pixels = img.load()
        
        # Encrypt each pixel
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                # Apply encryption: simple mathematical operation
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
        
        # Save the encrypted image
        img.save(output_path)
        print(f"Encrypted image saved to: {output_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(image_path, key, output_path):
    """Decrypts an image using reverse pixel manipulation."""
    try:
        # Open the encrypted image
        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = img.load()
        
        # Decrypt each pixel
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                # Reverse the encryption operation
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
        
        # Save the decrypted image
        img.save(output_path)
        print(f"Decrypted image saved to: {output_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

# Main function to demonstrate the tool
if __name__ == "__main__":
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Encrypt an image
        image_path = input("Enter the path of the image to encrypt: ").strip()
        key = int(input("Enter the encryption key (integer): "))
        output_path = input("Enter the path to save the encrypted image: ").strip()
        encrypt_image(image_path, key, output_path)
    
    elif choice == "2":
        # Decrypt an image
        image_path = input("Enter the path of the image to decrypt: ").strip()
        key = int(input("Enter the decryption key (same as encryption key): "))
        output_path = input("Enter the path to save the decrypted image: ").strip()
        decrypt_image(image_path, key, output_path)
    
    else:
        print("Invalid choice. Exiting.")
