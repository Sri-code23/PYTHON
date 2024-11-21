dicta={"l":"luffy","z":"zoro","s":"sanji"}
#print(dir(dicta))
#print(help(dicta))

print(dicta.get("sri"))
# output : None

"""

if dicta.get("f"):
    print("available")
else:
    print("not available")
    # output : not available
"""

#dicta.update({"s":"shark"})

#dicta.pop("s")
# output  : {'l': 'luffy', 'z': 'zoro'}


#dicta.popitem()
# output : ('s', 'sanji')

"""
values=dicta.values()
for i in values:
    print(i)
    # output : luffy
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
