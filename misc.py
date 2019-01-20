import requests


def get_content_from_url(url):
    return requests.get(url).content

def save_file(url, content):
    raise NotImplementedError
