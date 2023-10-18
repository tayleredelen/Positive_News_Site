import requests

# get image url by opening image in new tab
url = ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/2_Sphynx_cats_sleeping_together.jpg/440px"
       "-2_Sphynx_cats_sleeping_together.jpg")
# use requests to get url
response = requests.get(url)

# write the image into the project, use wb instead of just w
with open("image.jpg", "wb") as file:
    file.write(response.content)


