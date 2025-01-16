# Image Encryption Tool

A Python-based tool for encrypting and decrypting images using pixel manipulation techniques. This project allows users to securely encrypt their images by modifying pixel values and decrypt them using the same key.

---

## Features
- Encrypts and decrypts images by altering pixel values using a user-defined key.
- Outputs an encrypted image and restores the original image with the decryption key.
- Supports `.png`, `.jpg`, and other popular image formats.

---

## How It Works

1. **Encryption**:
   - Alters the RGB values of each pixel in the image using a mathematical operation and a secret key.
   - Outputs an encrypted image that appears distorted and unrecognizable.

2. **Install Dependencies**:
   - Make sure Python is installed and install the required library:
     ```bash
     pip3 install pillow
     ```

3. **Decryption**:
   - Reverses the encryption process using the same key.
   - Restores the original image.

---

## About Data

The tool processes images by manipulating the pixel values to perform encryption and decryption. Here's how the data is used:

- **Input Data**:
  - The input data is an image file in a common format such as `.png`, `.jpg`, or `.bmp`.
  - Users are prompted to enter a secret key during the encryption process, which is used to modify the pixel values.

- **Encryption Process**:
  - The pixel values are modified based on the secret key using a simple mathematical operation.
  - The encrypted image is saved with altered pixel data, making it unrecognizable to the human eye.

- **Decryption Process**:
  - The decryption process reverses the encryption operation, restoring the original pixel values if the correct key is provided.
  - The decrypted image should match the original image before encryption.

- **Output Data**:
  - The output of the encryption process is an encrypted image (`encrypted_image.png`) which appears as a scrambled, distorted image.
  - The output of the decryption process is the original image, saved as `decrypted_image.png`.

---

## Usage

### 1. Clone the Repository:
```bash
git clone https://github.com/Sachin-1402/image-encryption-tool.git
```
```bash
cd image-encryption-tool
```




