#QR code decoder
import cv2
detector = cv2.QRCodeDetector()
reval,point,s_qr = detector.detectAndDecode(cv2.imread("mydetails_in_qr.png"))
print(reval)