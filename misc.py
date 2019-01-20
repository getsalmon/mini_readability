import urllib.parse

import requests

import config


def get_content_from_url(url):
    headers = {}
    url = urllib.parse.unquote(url)
    if config.user_agent is not None and config.user_agent != '':
        headers['User-Agent'] = config.user_agent
    try:
        return requests.get(url, headers=headers).content
    except Exception as e:
        print('Не удалось скачать статью по адресу: {}. '
              'Ошибка: {}'.format(url, e))
