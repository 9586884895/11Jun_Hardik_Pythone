import requests
import pandas as pd

url="https://fakestoreapi.com/products/"

req=requests.get(url)

data=req.json()

#print(data)
y=pd.DataFrame(data)
print(y[['id','title','price':'pid','ptitle','priceds']],inplace=true)

"""for i in data:
    print(f"ID:{i["id"]}")
    print(f"ID:{i["title"]}")
    print(f"ID:{i["price"]}")
    print("----------------------------")"""
   
