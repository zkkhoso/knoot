import requests
import json
import os
import time

def get_fb_user_info(access_token, user_id):
    url = f"https://graph.facebook.com/{user_id}?access_token={access_token}&fields=id,name,email,location,work,education"
    response = requests.get(url)
    return response.json()

def get_fb_user_posts(access_token, user_id):
    url = f"https://graph.facebook.com/{user_id}/posts?access_token={access_token}&fields=id,message,created_time"
    response = requests.get(url)
    return response.json()

def get_fb_user_friends(access_token, user_id):
    url = f"https://graph.facebook.com/{user_id}/friends?access_token={access_token}&fields=id,name"
    response = requests.get(url)
    return response.json()

def clone_fb_account(access_token, user_id, clone_id):
    user_info = get_fb_user_info(access_token, user_id)
    user_posts = get_fb_user_posts(access_token, user_id)
    user_friends = get_fb_user_friends(access_token, user_id)

    # Create a new Facebook account with the same info
    new_user_info = {
        "id": clone_id,
        "name": user_info["name"],
        "email": user_info["email"],
        "location": user_info["location"],
        "work": user_info["work"],
        "education": user_info["education"]
    }

    # Create a new Facebook account with the same posts
    new_user_posts = []
    for post in user_posts["data"]:
        new_post = {
            "id": post["id"],
            "message": post["message"],
            "created_time": post["created_time"]
        }
        new_user_posts.append(new_post)

    # Create a new Facebook account with the same friends
    new_user_friends = []
    for friend in user_friends["data"]:
        new_friend = {
            "id": friend["id"],
            "name": friend["name"]
        }
        new_user_friends.append(new_friend)

    # Save the cloned account info to a file
    with open("cloned_account.json", "w") as f:
        json.dump({
            "user_info": new_user_info,
            "user_posts": new_user_posts,
            "user_friends": new_user_friends
        }, f, indent=4)

def main():
    access_token = input("Enter your Facebook access token: ")
    user_id = input("Enter the user ID you want to clone: ")
    clone_id = input("Enter the ID for the cloned account: ")

    clone_fb_account(access_token, user_id, clone_id)

    print("Account cloned successfully!")

if __name__ == "__main__":
    main()