import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Githib User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser') #produces raw html content
profile_image_element = soup.find('img', {'class': "avatar avatar-user width-full border color-bg-default"}) #Finds profile image
if profile_image_element:
    profile_image = profile_image_element['src']
    print(profile_image)
else:
    print("Profile image not found.")

