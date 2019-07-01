import sys
import time
from itertools import count
from urllib.request import Request, urlopen

from selenium import webdriver

from collection.crawler import crawling
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def crawling_pelicana():
    results = []
    for page in count(100):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page={0}'.format(page)
        html = crawling(url=url, encoding='utf-8')
        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class':'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')
        #end point
        if len(tags_tr) == 0:
            break
        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]
            t = (name, address) + tuple(sidogu)
            results.append(t)
        # store
        table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)


def crawling_nene():
    results = []
    compare = bs4.element.Tag
    for page in count(1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page={0}&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'.format(page)
        html = crawling(url=url, encoding='utf-8')
        bs = BeautifulSoup(html, 'html.parser')
        tags_shopinfo = bs.findAll('div', attrs={'class': 'shopInfo'})
        if compare == tags_shopinfo[0]:
            print('end ', page)
            break;
        compare = tags_shopinfo[0]
        print(page)
        for tag_shopinfo in tags_shopinfo:
            tags_shopname = tag_shopinfo.find('div', attrs={'class': 'shopName'})
            tags_shopadd = tag_shopinfo.find('div', attrs={'class': 'shopAdd'})
            t = (tags_shopname.text, tags_shopadd.text)
            results.append(t)
    table = pd.DataFrame(results, columns=['name', 'address'])
    table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)



def crawling_kyochon():
    for sido1 in range(1, 2):
        for sido2 in range(1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)
            html = crawling(url)

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_spans = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tags_spans:
                strings = list(tag_span.strings)
                print(strings)
                name = strings[1]
                address = strings[3].replace('\r\n\t', '').strip()
                print(name, address, sep=':')


def crawling_goobne():
    url = 'http://www.goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('D:\cafe24\chromedriver\chromedriver.exe')
    wd.get(url)
    time.sleep(3)
    results = []
    for page in range(1, 2):
        script = 'store.getList(%d)' %page
        wd.execute_script(script)
        time.sleep(3)
        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.findAll('tbody', attr = {'id':'store_list'})
        # tags_tr = tag_tbody.findAll('tr')
        # print(tags_tr)
        print(tag_tbody)

if __name__ == '__main__':
    # crawling_pelicana()
    crawling_nene()
    # crawling_kyochon()
    # crawling_goobne()