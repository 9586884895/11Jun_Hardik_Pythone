import requests

"""class studinfo:
    def __init__(self):
        print("This is My init class")

st=studinfo()"""

class internet:
    def __init__(self):        
        url="https://careercenter.tops-int.com/"
        if requests.get(url):
            print("internet Excess ok")
        else:
            print("Internet connection not available!")

c=internet()