import requests
import base64

def change_profile_picture(token, image_path):
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
        print('Sucess! Profile Picture Added !')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    token = input("Enter your bot token: ")
    gif_path = input("Enter the path to your GIF file: ")
    change_profile_picture(token, gif_path)

if __name__ == "__main__":
    main()
    input('press any key to quit....')
