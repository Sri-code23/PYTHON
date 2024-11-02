dicta={"l":"luffy","z":"zoro","s":"sanji"}
#print(dir(dicta))
#print(help(dicta))

#print(dicta.get("sri"))
"""

if dicta.get("f"):
    print("available")
else:
    print("not available")
"""

#dicta.update({"s":"shark"})

#dicta.pop("s")

#dicta.popitem()

"""
values=dicta.values()
for i in values:
    print(i)
"""

"""
keys=dicta.keys()
for i in keys:
    print(i)
"""
#items=dicta.items()
for keys, values in dicta.items():
    print(f"{keys}:{values}")

print(dicta)
