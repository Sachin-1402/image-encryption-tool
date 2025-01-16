# Image Encryption Tool

A Python-based tool for encrypting and decrypting images using pixel manipulation techniques. This project allows users to securely encrypt their images by modifying pixel values and decrypt them using the same key.

---

## Features
- Encrypts images by altering pixel values using a user-defined key.
- Decrypts encrypted images to restore the original content with the correct key.
- Easy-to-use interface with minimal setup required.
- Supports `.png`, `.jpg`, and other popular image formats.

---

## How It Works
1. **Encryption**:
   - Alters the RGB values of each pixel in the image using a mathematical operation and a secret key.
   - Outputs an encrypted image that appears distorted and unrecognizable.

2. **Decryption**:
   - Reverses the encryption process using the same key.
   - Restores the original image.

---

## Usage

### 1. Clone the Repository:
### 2. Install dependencies
Make sure Python is installed and install the required library:

```bash


git clone https://github.com/Sachin-1402/image-encryption-tool.git
cd image-encryption-tool
---
pip3 install pillow

python3 image_encryption.py






###2. Install Dependencies:
Make sure Python is installed and install the required library:

```bash
pip3 install pillow
