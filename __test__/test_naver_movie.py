from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection.crawler import crawling


def naver_movie_rank(data):
    bs = BeautifulSoup(data, 'html.parser')
    result = bs.findAll('div', attrs={'class': 'tit3'})
    return result

def naver_movie_view(data):
    for index, div in enumerate(data):
        print(index +1, div.a['title'], div.a['href'], sep = ' : ')

def ex02():
    crawling(url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn', encoding='cp949',proc1=naver_movie_rank,
             proc2=lambda data: list(map(lambda div: print(div[0]+1, div[1].a.text, div[1].a['href'], sep=':'), enumerate(data))))

def ex01():
    request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)

    html = response.read().decode('cp949')  # python에서의 euc-kr

    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())
    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep=":")
    print('=====================================================')

__name__ =='__main__' and not ex01() and not ex02()