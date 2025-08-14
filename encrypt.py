from PIL import Image
import numpy as np

input_path = "./input/input.png"

image = Image.open(input_path).convert('RGB')
image_array = np.array(image, dtype=np.uint8)

h, w, channel = image_array.shape 
#key
key = np.random.randint(0, 256, size=(h,w,channel), dtype=np.uint8)

# Lưu Key
key_path = './key/key.npy'
np.save(key_path, key)
print("saved key")

# #encrypt: cộng modulo 256.
# Z256
encrypt_arr = (image_array.astype(np.int32) + key.astype(np.int32)) % 256
encrypt_arr = encrypt_arr.astype(np.uint8)

# Lưu ảnh
encrypt_img = Image.fromarray(encrypt_arr)
output_path_encrypted = "./output/encrypted.png"
encrypt_img.save(output_path_encrypted)
print("image encrypted")


