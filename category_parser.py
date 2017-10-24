import requests
from lxml import etree
from phone_parser import get_phone

headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
                'Accept': 'application/json',
                'Accept-Language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                'Accept-Encoding': 'gzip, deflate, br',
                'x-requested-with': 'XMLHttpRequest',
                'Host': 'm.avito.ru',
                'Proxy-Authorization': 'Basic Og==',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache'
}


def parse_category(link):
    response = requests.get(link, headers=headers)
# root = etree.Element("root")
    root = etree.HTML(response.text)
    for i in range(1,22):
        url = root.xpath("/html/body/section/article[{}]/div/a/@href".format(str(i)))[0]
        phone = get_phone(url, headers)
        print(url, phone)

parse_category('https://m.avito.ru/moskva/transport')