import requests
import pandas

url="https://fakestoreapi.com/products/"

req=requests.get(url)

data=req.json()

#print(data)
y=pandas.DataFrame(data)
print(y)

"""for i in data:
    print(f"ID:{i["id"]}")
    print(f"ID:{i["title"]}")
    print(f"ID:{i["price"]}")
    print("----------------------------")"""
   
