import os
from logging import raiseExceptions

import requests

def get_extension(image_url : str)->str |None:
    extension : list[str] = ['.png','.jpg']
    for ext in extension:
        if ext in image_url:
            return ext
def download_image(image_url:str, name:str, folder: str = None):
    if ext:= get_extension(image_url):
            if folder:
                image_name : str =f"{folder}/{name}{ext}"
            else:
                image_name:  str = f'{name}{ext}'
    else:
        raise Exception("Image extrnsion could not be located")

    if os.path.isfile(image_name):
        raise Exception("File name already exists")

    try:
        image_contente : bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            print(f"Downloaded {image_name} successfully")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    input_url : str = input("Enter a url ")
    input_name : str = input("what would you like to name it: ")
    print("Downloading....")
    download_image(input_url, name=input_name, folder='images')

