import pyqrcode 

# 生成 QRCode
s = "https://www.baidu.com"

url = pyqrcode.create(s)

url.svg("./baidu.svg",scale=8)

url.png('./code.png',scale=5,module_color="#7D007D")