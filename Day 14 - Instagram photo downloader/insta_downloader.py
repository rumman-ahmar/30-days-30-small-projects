import requests
from bs4 import BeautifulSoup


def get_instagram_photo_url(url):
    # make request
    response = requests.get(url)
    # create soup
    soup = BeautifulSoup(response.text, 'html.parser')
    # find metadata and og:image attribute
    meta_tags = soup.find_all('meta')
    for tag in meta_tags:
        if tag.get('property', None) == 'og:image':
            return tag.get('content', None)
    return


def download_instagram_photo(url, filename):
    # make request
    response = requests.get(url)
    # save image
    with open(filename, 'wb') as file:
        file.write(response.content)
    return


if __name__ == '__main__':
    url = 'https://www.instagram.com/p/CivwPTNPquf/'
    filename = 'instagram_photo.jpg'
    photo_url = get_instagram_photo_url(url)
    download_instagram_photo(photo_url, filename)
