import qrcode

data=f"Name:-Bigfly Enterprise\nAcc.No:-0003110100005743\nIFSC Code:-YESB0RAJ003\nContact:- Dineshbhai Vegda(9825145970)\nAddress:-Shed no 16,17,18, Jay industrial estate\nopp.mascot Electro,J.J.Solar street\nBhumi Polymer gate\n Shapar(Veraval) Pin:-360024"
qr=qrcode.make(data)
qr.save("Big.png")