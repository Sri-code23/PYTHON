#requests is used to access the api url
import requests

#paste the base link of the desired api url to retrieve data
api_url="  " 

def get_info(name):
    #to join the base url with the requesting data
    url=f"{api_url}/path/{name}"
    #response is an object that stores the requests.get(url) which access the informtion from api
    response=requests.get(url)
#if we print response here it return the url status code  (200 - is okay)

    if response.status_code==200:
        #if the status code is satisfied the response data is imported in json format
        data=response.json()
        #if we print data here the data is vast and unesy to read the information
        return data
    
    else:
        print("failed to retrieve data ")


name="rgher "
#if the get_info(name) exists then reply becomes true
reply=get_info(name)


if reply:
    #retrieving the data of a specific field like data1.data2,data3...(name,age,...)
    print(f" data1: { reply[data1]}")
    print(f" data2: { reply[data2]}")
    print(f" data3: { reply[data3]}")
    print(f" data4: { reply[data4]}")