import cv2
import string
import os
# Function to apply reverse Caesar Cipher (-3 shift)
def decrypt_text(text):
    return ''.join(chr((ord(char) - 3) % 256) for char in text)
# Load Encoded Image
image_path = input("Enter encoded image path: ")
img = cv2.imread(image_path)
if img is None:
    print("Error: Image not found!")
    exit()
# Get Password
password = input("Enter passcode: ")
# Extract Message
extracted_text = ""
for row in img:
    for pixel in row:
        char = chr(pixel[0])  # Read Red channel
        extracted_text += char
        if extracted_text.endswith("|END"):
            extracted_text = extracted_text.replace("|END", "")
            break
# Decrypt the message
decrypted_text = decrypt_text(extracted_text)
# Validate Password
if "|" in decrypted_text:
    stored_pass, message = decrypted_text.split("|", 1)
    if stored_pass == password:
        print("Decrypted Message:", message)
    else:
        print("Incorrect password! Access denied.")
else:
    print("Decryption failed. Delimiter '|' not found in the decrypted text.")




