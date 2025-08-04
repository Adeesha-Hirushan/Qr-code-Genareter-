from PIL import Image
from pyzbar import pyzbar

img = Image.open("qr1.png")
out = pyzbar.decode(img)
print(out[0][0].decode('utf-8'))