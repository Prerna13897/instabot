import requests
App_Access_token = "5000190155.fc9a349.697c42586a294b6db99b941b0f84f1a2"
BASE_URL = "https://api.instagram.com/v1/"
def admin_info():
    owner_url = BASE_URL + "users/self/?access_token=" + App_Access_token   #https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
    owner_info = requests.get(owner_url).json()                             #Get information about the owner of the access_token
    print owner_info
    print owner_info["data"]["username"]
    print owner_info["data"]["bio"]
admin_info()

def client_search_by_username(insta_user):
    client_url=BASE_URL+"users/search?q="+insta_user+"&access_token="+App_Access_token   #https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
    client_info=requests.get(client_url).json()                                   #search for user by name
    print client_info
    return client_info["data"][0]["id"]
client_search_by_username("rk_chaudhary300")
