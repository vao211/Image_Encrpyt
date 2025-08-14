from PIL import Image
import numpy as np

encrypted_img_path = "./output/encrypted.png"
encrypted_img = Image.open(encrypted_img_path).convert("RGB")

encrypted_arr = np.array(encrypted_img, dtype=np.uint8)

# load key
key_path = "./key/key.npy"
key = np.load(key_path)

# Decrypt: nghịch đảo trong nhóm (trừ modulo 256)
decrypted_array = (encrypted_arr.astype(np.int32) - key.astype(np.int32)) % 256
decrypted_array = decrypted_array.astype(np.uint8)

# Lưu ảnh
decrypted_image = Image.fromarray(decrypted_array)
output_path_decrypted = './output/decrypted.png'
decrypted_image.save(output_path_decrypted)


original_path = "./input/input.png"
original_array = np.array(Image.open(original_path).convert('RGB'), dtype=np.uint8)
match = np.all(decrypted_array == original_array)
print(f"Decrypted matches original: {match}")

#in vị trí khác biệt
if not match:
    diff = np.where(decrypted_array != original_array)
    print("Positions where decrypted differs from original:", diff)
    
