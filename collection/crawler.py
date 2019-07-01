import ssl
import sys
from urllib.request import Request, urlopen


def crawling(url='', encoding='utf-8', proc1=lambda data: data, proc2=lambda data: data, err=lambda e: print('except : ', e, file=sys.stderr)):
    try:
        request = Request(url)
        context = ssl._create_unverified_context()
        response = urlopen(request, context=context)
        receive = response.read()
        html = receive.decode(encoding, errors='replace')
        result = proc2(proc1(html))
        return result
    except Exception as e:
        print('except : ', e, file=sys.stderr)
