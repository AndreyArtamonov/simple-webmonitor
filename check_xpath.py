import sys

import requests
from lxml import html
from fake_useragent import UserAgent

headers = {'user-agent': UserAgent().chrome}

url = 'http://localhost/'
xpath = '//div[@class="test"]/text()'

page = requests.get(url, headers=headers)
page = html.fromstring(page.text).xpath(xpath)

print(page)