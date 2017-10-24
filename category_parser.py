import requests
from lxml import etree
from phone_parser import get_phone

headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36',
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
    print(response.text)
    root = etree.HTML(response.text)
    for i in range(1,22):
        url = root.xpath("/html/body/section/article[{}]/div/a/@href".format(str(i)))[0]
        phone = get_phone(url, headers)
        with open('phone.txt') as f:
            f.write(phone)
        print(phone)

for i in range(1, 10):
    parse_category('https://m.avito.ru/moskva/transport?p={}'.format(str(i)))