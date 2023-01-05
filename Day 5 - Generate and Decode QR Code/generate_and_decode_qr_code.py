import qrcode
import cv2

# generate QR code
img = qrcode.make("www.google.com")
# save QR code as png image
img.save('google.png')

# make object
detector = cv2.QRCodeDetector()

# decode QR code
value, points, qr_code = detector.detectAndDecode(
    cv2.imread("google.png"))

# print the decoded value of the QR code
print(value)
