from email.mime import image
from genericpath import exists
import requests
import os
import sys
from bs4 import *

# folder creation
def create_folder(images):
    try:
        folder_name = input("Enter a folder name: ")
        os.makedirs(folder_name, exist_ok=True)

    # request another name if folder exists with that name
    except:
        print("Folder already exists with that name!")
        create_folder()

    download_images(images, folder_name)

# download images and store in folder
def download_images(images, folder_name):
    count = 0
    print(f'{len(images)} images found')

    if len(images)>0:
        for i,image in enumerate(images):
            try:
                # check src attribute for image
                image_link = image['src']
            except:
                # no src attribute
                print("no src attribute")
                continue

            # check if it is a png image or skip
            if ".png" in image_link or ".PNG" in image_link:
                # get content of image from source url
                try:
                    r = requests.get(image_link).content

                    # download images into folder
                    with open(f'{folder_name}/image{i+1}.png',"wb+") as f:
                        f.write(r)

                    count+=1
                except:
                    pass
            else:
                print("not png")
                continue
        print(f'{count} PNG images(with src)/{len(images)} total images downloaded')


# before
# for arg in sys.argv:
#     print(arg)
# # limit to 2 arguments
# if(len(sys.argv)>3):
#     sys.exit('args should not exceed 2')

# # url = 'http://google.com/favicon.ico'
# # save_path = 'myfolder'
# url = sys.argv[1]
# save_path = sys.argv[2]
# os.makedirs(f'Streets/{save_path}', exist_ok=True)
# r = requests.get(url, allow_redirects=True)
# open(f'Streets/{save_path}/favicon.ico', 'wb').write(r.content)

# before

def main(url,username,password):

    # get content of the url and allow redirection
    r = requests.get(url, allow_redirects=True)

    # parse HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in page
    images = soup.findAll('img')

    create_folder(images)

# inputs
url = input("Enter URL to download images from:\n")
username = input("Enter username(optional):\n")
password = input("Enter password(optional):\n")

main(url,username,password)

