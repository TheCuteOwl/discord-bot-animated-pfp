import requests
import base64
import os
import sys

def is_valid_token(token):
   """
   Check if the token is valid.

   :param token: The token to check.
   :return: True if the token is valid, False otherwise.
   """
   return len(token.strip()) > 0

def is_valid_image_path(image_path):
   """
   Check if the given image path is valid.

   :param image_path: The path to the image file.
   :return: True if the image path is valid, False otherwise.
   """
   return os.path.isfile(image_path) and not image_path.endswith('~')

def display_error_and_exit(error_message):
   """
   Display an error message and exit the application.

   :param error_message: The error message to display.
   """
   print(f'Error: {error_message}')
   sys.exit(1)

def get_user_input():
   """
   Retrieve user input for the bot token and image path.

   :return: A tuple containing the token and image path.
   """
   token = input("Enter your bot token (don't share it with anyone): ")
   if not is_valid_token(token):
       display_error_and_exit("Invalid token. Please enter a valid token.")

   image_path = input("Drag and drop your image file here and press Enter: ")
   if not is_valid_image_path(image_path):
       display_error_and_exit("Invalid image path. Please provide a valid image file.")

   return token, image_path

def change_profile_picture(token, image_path):
   """
   Change the profile picture for the user associated with the given token.

   :param token: The bot token.
   :param image_path: The path to the image file.
   """
   try:
       with open(image_path, "rb") as image_file:
           encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

       headers = {
           "Authorization": f"Bot {token}",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
           "Content-Type": "application/json"
       }

       data = {
           "avatar": f"data:image/png;base64,{encoded_image}"
       }

       url = "https://discord.com/api/v9/users/@me"
       response = requests.patch(url, headers=headers, json=data)

       if response.status_code != 200:
           print(f"An error occurred: {response.json()}")
           return

       print('Success! Profile Picture Added!')
   except Exception as e:
       print(f"An error occurred: {e}")

def main():
   """
   The main function, responsible for user input and calling the necessary functions.
   """
   try:
       token, image_path = get_user_input()
       change_profile_picture(token, image_path)
   except Exception as e:
       print(f"An error occurred: {e}")
       sys.exit(1)

if __name__ == "__main__":
   main()