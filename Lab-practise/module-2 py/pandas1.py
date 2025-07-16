import pandas

stdata={
    "s":[1,2,3,4,5],
    "name":["Hardik","Jayesh","Ramesh","Durgesh","Parth"],
    "city":["rajkot","Jamnagar","Jungadh","porbandar","gariyadhar"]
}

data=pandas.DataFrame(stdata)
print(data)

