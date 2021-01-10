import pyqrcode
import png

from pyqrcode import QRCode


link = input('Enter the URL to generate the QR Code: ')

url = pyqrcode.create(link)
url.png("./qr.png", scale=5)
