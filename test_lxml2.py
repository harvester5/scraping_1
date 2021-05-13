# Сверка по времени

import win_unicode_console

win_unicode_console.enable()
import time
import requests
import lxml.html


class OlxParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.last_time = ''

    def get_page(self):
        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return
        if res.status_code < 400:
            return res.content

    def parse(self, html):
        html_tree = lxml.html.fromstring(html)
        print(html_tree)
      #  tree = etree.parse(html)


#        nodes = html.xpath('/html/body/div')

#        print(etree.tostring(html))


#        path = ".//table[@id='offers_table']//td[@class='offer  ']"
 #       last_offer = html_tree.xpath(path)[0]
#        print(last_offer.text_content())

#        link = last_offer.xpath('.//a')[1].get('href')
#        print(link)

#        cur_time = last_offer.xpath('./table/tbody/tr[2]//p')
        # print(cur_time)
#        for p in cur_time:  # 00:37:34
#            print('---')
#            print(p.text_content)

    def run(self):
        pass


if __name__ == "__main__":
    parser = OlxParser('https://www.mamba.ru/ru/search/list')
    page = parser.get_page()
    parser.parse(page)