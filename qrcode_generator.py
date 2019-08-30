
# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode


# String which represent the QR code
s = "Your_link/url.com"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png("yourawesome_qrcode.png", scale = 8)
