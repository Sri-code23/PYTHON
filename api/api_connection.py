import requests

base_url="https://pokeapi.co/api/v2/"

def get_info(char_name):
    url=f"{base_url}pokemon/{char_name}"
    response=requests.get(url)
    data=response.json()
    return data
    

char_name="pikachu"    
res=get_info(char_name)
if res:
   print(f"name:{res['name']}")
   print(f"id:{res['id']}")
   print(f"height:{res['height']}metre ")
