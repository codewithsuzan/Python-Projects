import qrcode as qr
img=qr.make("https://github.com/codewithsuzan")
img.save("qrcode.png")
print("QR code generated successfully.")