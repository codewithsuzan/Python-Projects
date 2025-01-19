import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://github.com/codewithsuzan")

qr.make(fit=True)

img=qr.make_image(fill="red", back_color="blue")

img.save("qr_code2.png")

print("QR code saved successfully!")
