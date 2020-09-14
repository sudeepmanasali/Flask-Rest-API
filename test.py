
import requests

BASE = "http://127.0.0.1:5000/"
k=1
response = requests.post(BASE + "helloworld",data={"data":k})
print(response.json())