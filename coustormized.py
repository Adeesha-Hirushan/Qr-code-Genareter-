import qrcode

qr = qrcode.QRCode(border=5, box_size=9)

qr.add_data("Welcome Back!")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("custom_qr.png")