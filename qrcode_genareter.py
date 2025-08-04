import qrcode

data = " Input your data..."

img = qrcode.make(data)

img.save("qr1.png")