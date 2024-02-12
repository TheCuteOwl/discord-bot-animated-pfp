import requests
import base64

def change_profile_picture(token, image_path):
    try:
        image_path = image_path.replace('"',"")
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
        print('Success! Profile Picture Added!')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    token = input("Enter your bot token: ")
    image_path = input("Drag and drop your GIF file here and press Enter: ")
    change_profile_picture(token, image_path)

if __name__ == "__main__":
    main()
