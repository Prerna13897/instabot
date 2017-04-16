# ______________________________________________________INSTABOT_______________________________________________________________________#
import requests
App_Access_token = "5000190155.fc9a349.697c42586a294b6db99b941b0f84f1a2"
BASE_URL = "https://api.instagram.com/v1/"
def admin_info():
    owner_url = BASE_URL + "users/self/?access_token=" + App_Access_token   #https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
    owner_info = requests.get(owner_url).json()                             #Get information about the owner of the access_token
    #print owner_info
    print ("_____________owner_info______________")
    print("Name                    : ", owner_info['data']['full_name'])
    print("Username                : ", owner_info['data']['username'])
    print("Link to Profile Picture : ", owner_info['data']['profile_picture'])
    print("Media Shared            : ", owner_info['data']['counts']['media'])
    print("Followed By             : ", owner_info['data']['counts']['followed_by'])
    print("Followers               : ", owner_info['data']['counts']['follows'])
    if owner_info['data']['website'] != '':
        print("Website                 : ", owner_info['data']['website'])
    else:
        print("Website                 :  No Website Available")
    if owner_info['data']['bio'] != '':
        print("Bio                     : ", owner_info['data']['bio'])
    else:
        print("Bio                     :  No Info Available")
#admin_info()

def client_search_by_username(username):                                    #search for user by username
    client_url=BASE_URL+"users/search?q="+username+"&access_token="+App_Access_token    #Get a list of users matching the query
    client_info=requests.get(client_url).json()                              #The function should make a GET call to search user with the particular username
    #print client_info
    if client_info['data'] == []:
           print("sorry!!!!User with giving username doesn't exist")           #If the user is not found then the function should print a meaningful message
           return 0
    else:
        user_id = client_info['data'][0]['id']    #If multiple users are found the function should accept the first one
        return user_id                                                       #Upon successful search, the function should return the user's id

#client_search_by_username("manpreet287")#https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
def info_of_user(username):     #search for user by username
    user_id=client_search_by_username(username)
    client_url=BASE_URL+"users/"+user_id+"/?access_token="+App_Access_token    #Get a list of users matching the query
    client_info=requests.get(client_url).json()                              #The function should make a GET call to search user with the particular username
    #print client_info
    if client_info['data'] == []:
           print("sorry!!!!User with giving username doesn't exist")           #If the user is not found then the function should print a meaningful message
           return 0
    else:
        print("____________________client_info_______________")
        print("Name                    : ", client_info['data']['full_name'])
        print("Username                : ", client_info['data']['username'])
        print("Link to Profile Picture : ", client_info['data']['profile_picture'])
        print("Media Shared            : ", client_info['data']['counts']['media'])
        print("Followed By             : ", client_info['data']['counts']['followed_by'])
        print("Followers               : ", client_info['data']['counts']['follows'])
        if client_info['data']['website'] != '':
            print("Website                 : ", client_info['data']['website'])
        else:
            print("Website                 :  No Website Available")
        if client_info['data']['bio'] != '':
            print("Bio                     : ", client_info['data']['bio'])
        else:
            print("Bio                     :  No Info Available")

def get_user_post_id(username):
    if username not in ['manpreet287', 'rk_chaudhary300']:
        print"you enter wrong wrong username"
        return
    else:
     insta_user_id=client_search_by_username(username)                 #The function should make use of the above created function to fetch the user's Id using the username.
     request_url= BASE_URL+"users/"+insta_user_id+"/media/recent/?access_token="+App_Access_token    #https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    #print request_url                                                                                #Get the total no of recent media published by a user.
     request_to_get_all_post = requests.get(request_url).json()
     if len(request_to_get_all_post["data"])== 0:
        print("\nNo Posts Found for this User !")
     else :
        posts =len(request_to_get_all_post["data"])
        total_posts = str(posts)
        print(" The " + username + " have " + total_posts + " total posts.")
        post_ids = []
        post_likes = []
        post_comments = []
        post_links = []
        for media in (request_to_get_all_post['data']):
            post_ids.append(media['id'])
            post_likes.append(media['likes']['count'])
            post_comments.append(media['comments']['count'])
            post_links.append(media['link'])
        print("\nWhich Recent Post you want to select ?")
        print("1. The post having maximum likes.")
        print("2. The post having minimum likes.")
        print("3. The post on the basis of comments.")
        print("\n Enter your choice from 1 or 2 or 3\n")
        choice=raw_input()
        if int(choice) == 1:
            dictionary = dict(zip(post_ids, post_likes))
            dictionary = sorted(dictionary, key=dictionary.__getitem__)
            max_likes = max(post_likes)
            return dictionary[max_likes],post_links[max_likes]
        elif int(choice) == 2:
            dictionary = dict(zip(post_ids, post_likes))
            dictionary = sorted(dictionary, key=dictionary.__getitem__)
            min_likes = min(post_likes)
            return dictionary[min_likes],post_links[min_likes]
        elif int(choice) == 3:
            dictionary = dict(zip(post_ids, post_comments))
            dictionary = sorted(dictionary, key=dictionary.__getitem__)
            min_comments = min(post_comments)
            return dictionary[min_comments], post_links[min_comments]
        else:
            print("You entered the wrong choice. Please choose from given options.")
        choice = input("\nEnter your choice (1 or 2 or 3 ) : ")


def like_on_user_post_id(username):
    post_id,post_links=get_user_post_id(username)
    Access_token={'access_token':App_Access_token}                                             #To like a user_post
    url_post_like= BASE_URL+"media/"+str(post_id)+"/likes"
    data=requests.post(url_post_like,Access_token).json()
    if data['meta']['code'] == 200:
        print("The post has been liked.")
    else:
        print("Some error occurred! Try Again.")
#like_on_user_post_id("manpreet287")

def comment_on_user_id(username):
    post_id,post_link=get_user_post_id(username)
    url_post_comment = BASE_URL + "media/" +post_id+ "/comments"
    print ("enter the commant u want to post.\nNOTE THAT\nThe total length of the comment cannot exceed 300 characters.\nThe comment cannot contain more than 4 hashtags.\nThe comment cannot contain more than 1 URL\nThe comment cannot consist of all capital letters.\n")
    text=raw_input()
    text=str(text)
    Access_token_Plus_comment = {'access_token': App_Access_token, 'text': text}
    data = requests.post(url_post_comment, Access_token_Plus_comment).json()
    if data['meta']['code'] == 200:
        print("\nYour comment has been Posted.")
    else:
        print("\nSome error occurred! Try Again.")


#comment_on_user_id("manpreet287")
def search_comment_id(username): # for searching a paricular comment from post id of gien user username
    post_id,post_link=get_user_post_id(username)
    print ("Enter the word you want to search in comments of most interesting post : ")
    search = raw_input()
    word_to_be_searched = str(search)
    url = BASE_URL + "media/" + str(post_id) + "/comments/?access_token=" + App_Access_token
    request_comments = requests.get(url).json()
    list_of_comments = []
    comments_id = []
    user = []
    for comment in request_comments["data"]:
        list_of_comments.append(comment["text"])
        comments_id.append(comment["id"])
        user.append(comment["from"]["username"])
    comments_found = []
    comments_id_found = []
    user_found = []
    for i in range(0,len(list_of_comments),1):
        if word_to_be_searched in list_of_comments[i]:
            comments_found.append(list_of_comments[i])
            comments_id_found.append(comments_id[i])
            user_found.append(user[i])
    if len(comments_found) == 0:
        print("no comment have found that have the word \'%s\'" % word_to_be_searched)
        return False, post_id, False, False
    else:
        print("Following comments contains the word \'%s\'" % word_to_be_searched)
        for i in range(len(comments_found)):
            print(str(i+1) + ". " + comments_found[i])
        return comments_id_found, post_id, comments_found, user_found

#search_comment_id("manpreet287")

def delete_comment(username):
    comments_id_found,post_id,comments_found,user_found=search_comment_id(username)
    if(comments_found==0):
      print("Can't delete because there is no such comment in post_id= \'%s' " %  post_id)
      return False, post_id, False, False
    else:
      for i in range(len(comments_id_found)):
        url = BASE_URL + "media/" + str(post_id) + "/comments/" + str(comments_id_found[i]) + "/?access_token=" + App_Access_token
        data = requests.delete(url).json()
        if data['meta']['code'] == 200:
           print("%s --> Deleted." % comments_found[i])
           break
        elif data['meta']['error_code'] == "You cannot delete this comment":
            print("%s --> %s as it is made by %s." % (comments_found[i], data['meta']['error_code'], user_found[i]))
        else:
            print("Some error occurred. Try Again Later!!")







