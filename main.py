# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# Matn yoki link (QR code ichida bo‘ladi)
s = "www.geeksforgeeks.org"

# QR code yaratish
url = pyqrcode.create(s)

# QR code’ni SVG fayl sifatida saqlash
url.svg("myqr.svg", scale=8)

# QR code’ni PNG fayl sifatida saqlash
url.png("myqr.png", scale=6)
