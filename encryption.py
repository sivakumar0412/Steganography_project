import cv2
import os
import string
# Load image
image_path = input("Enter image path: ")
img = cv2.imread(image_path)
if img is None:
    print("Error: Could not load image!")
    exit()

# Get inputs
message = input("Enter secret message: ")
password = input("Enter passcode: ")

# Encrypt using Caesar Cipher
encrypted_text = ""
for char in f"{password}|{message}|END":
    encrypted_text += chr((ord(char) + 3) % 256)

# Convert to ASCII values
ascii_values = [ord(c) for c in encrypted_text]
print(f"Encrypted ASCII values ({len(ascii_values)}): {ascii_values[:50]}...")  # Debug

# Embed in image
index = 0
embedded = False
for row in img:
    for pixel in row:
        if index < len(ascii_values):
            pixel[0] = ascii_values[index]  # Modify Red channel
            index += 1
        else:
            embedded = True
            break
    if embedded:
        break

# Save result
output_path = "encoded_image.png"
cv2.imwrite(output_path, img)
print(f"Saved encoded image to {output_path} ({os.path.getsize(output_path)} bytes)")

# Verify embedding
verify_img = cv2.imread(output_path)
if verify_img is None:
    print("Error: Failed to save encoded image!")
else:
    os.system(f"start {output_path}")  # Windows
