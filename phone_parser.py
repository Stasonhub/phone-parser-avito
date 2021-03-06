import requests
from lxml import etree


def get_phone(relation_link, fake_haders):
    avito = 'https://m.avito.ru'
    item_page = requests.get(avito + relation_link)
    print(item_page.url)
    root = etree.HTML(item_page.text)
    url = root.xpath("//a[contains(@class, 'js-action-show-number')]/@href")[0] + '?async'
    data = {'async': ''}
    response = requests.get('https://m.avito.ru{}'.format(url), headers=fake_haders, data=data)
    return response.text
