import requests

import config


def get_content_from_url(url):
    headers = {}
    if config.user_agent is not None and config.user_agent != '':
        headers['User-Agent'] = config.user_agent
    return requests.get(url, headers=headers).content
