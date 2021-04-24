import json
filname = 'numbers.json'
try:
        with open(filname) as f:
                username = json.load(f)
except FileNotFoundError:
        username = input("name? ")
        with open(filname,'w') as f:
                json.dump(username,f)
                print("two")
else:
        print(f"wlecom ，{username}")

