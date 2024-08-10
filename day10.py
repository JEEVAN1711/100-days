
import pyqrcode
s="https://www.instagram.com/jeevan__moorthi?igsh=anAzNXUwcmJjYnkz"
process=pyqrcode.create(s)
process.svg("qrcode1.svg", scale = 8)
process.png('qrcodel.png', scale = 10)
print("Program Completed")
