import requests

class main_class():
    class sub_class():
        def link_check(url):
            
            response_check=requests.get(url)
            if response_check.status_code==200:
                print("the URL works")
            else:
                print(f"response_status : {response_check.status_code}")

if __name__=="__main__":
    url="https://www.google.com"  # enter your URL here

    obj=main_class.sub_class.link_check(url)