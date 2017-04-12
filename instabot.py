import requests
App_Access_token = "5000190155.fc9a349.697c42586a294b6db99b941b0f84f1a2"
BASE_URL = "https://api.instagram.com/v1/"
def admin_info():
    owner_url = BASE_URL + "users/self/?access_token=" + App_Access_token   #https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
    owner_info = requests.get(owner_url).json()                             #Get information about the owner of the access_token
    print owner_info
    #print owner_info["data"]["username"]
    #print owner_info["data"]["bio"]
#admin_info()

def client_search_by_username(insta_user):
    client_url=BASE_URL+"users/search?q="+insta_user+"&access_token="+App_Access_token   #https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
    client_info=requests.get(client_url).json()                                   #search for user by name
   # print client_info
    return client_info["data"][0]["id"]
#client_info_by_username("api_17790")

def get_user_post_id(insta_username):
    insta_user_id=client_search_by_username(insta_username)
    request_url= BASE_URL+"users/"+insta_user_id+"/media/recent/?access_token="+App_Access_token    #https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    #print request_url                                                                               #Get the most recent media published by a user.
    request_for_user_to_get_all_post = requests.get(request_url).json()
    return request_for_user_to_get_all_post["data"][0]['id']
get_user_post_id("rk_chaudhary300")

def like_on_user_post_id(user_id):
    user_current_post_id=get_user_post_id(user_id)
    Access_token={'access_token':App_Access_token}                                             #To like a user_post
    url_post_like= BASE_URL+"media/"+(user_current_post_id)+"/likes"
    requests.post(url_post_like,Access_token).json()

def comment_on_user_id(user_id):
    user_current_post_id=get_user_post_id(user_id)
    Access_token_Plus_comment ={'access_token':App_Access_token,'text':"#kkt"}                #To comment on user_id
    url_post_comment= BASE_URL+"media/"+user_current_post_id+"/comments"
    requests.post(url_post_comment,Access_token_Plus_comment).json()

comment_on_user_id("rk_chaudhary300")
