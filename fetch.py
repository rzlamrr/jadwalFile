import json
import os
import sys
import time

import requests

thn = sys.argv[1:]
bln = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

with open('kabko.json') as f:
    data = json.load(f)

for t in thn:
    print(t)
    for b in bln:
        try:
            os.makedirs(f"{t}/{b}")
        except Exception:
            pass

        for x in data:
            if os.path.isfile(f"{t}/{b}/{x['id']}.json"):
                print(f"{t}/{b}/{x['id']}.json already exists")
            else:
                try:
                    jason = requests.get(
                        f"https://api.myquran.com/v1/sholat/jadwal/{x['id']}/{t}/{b}").json()
                    if jason['status'] is True:
                        with open(f"{t}/{b}/{x['id']}.json", 'w') as ff:
                            json.dump(jason, ff, indent=2, ensure_ascii=True)
                    else:
                        print(f"ERROR: {x['id']}/{t}/{b}")
                except Exception as e:
                    print(f"ERROR: {x['id']}/{t}/{b}")
                    continue
                time.sleep(1)
