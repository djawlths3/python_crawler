from bs4 import BeautifulSoup

html = '''<td class="title">
<div class="tit3">
<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
</div>
</td>'''


def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.td.div

def ex2():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.td.div.a
    print(tag['title'])

def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.find('td', attrs={'class':'title'})
    print(tag)

if __name__ == '__main__':
    # ex1()
    ex3()