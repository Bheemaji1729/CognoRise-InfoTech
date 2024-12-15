#QR code encoder
import qrcode
qr = qrcode.QRCode(version=5, box_size=5, border=2)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
mobile = int(input("Enter your mobile num: "))
data = {"Name":name,"Age":age,"Email":email,"Mobile number":mobile}
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(Fill_color="black",back_color="white")
img.save("mydetails_in_qr.png")
img.show()