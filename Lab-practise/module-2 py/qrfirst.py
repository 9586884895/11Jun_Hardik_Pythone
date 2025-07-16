import qrcode

url="https://careercenter.tops-int.com/"

qr=qrcode.make(url)

qr.save("location.png")

