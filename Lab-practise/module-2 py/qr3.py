import qrcode

url="https://www.instagram.com/ankitacreation603?igsh=MTcxMGxneHgwbnQ0cQ=="

qr=qrcode.make(url)
qr.save("Ankita.png")