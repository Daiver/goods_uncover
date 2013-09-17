import sys
from grab import Grab

def google_it(q, num=10):
    #pageaddr ='http://google.com/search?hl=en&as_q=%s&num=%s&as_qdr=%s' % ('+'.join(q.split()), str(num),'')
    pageaddr ='http://market.yandex.ru/search.xml?text=%s' % ('+'.join(q.split()))
    g = Grab()
    g.go(pageaddr)
    titles = g.doc.select('//div/h3').text_list()
    hrefs = g.doc.select('//div/h3/a/@href').text_list()
    return zip(titles, hrefs)

if __name__ == '__main__':
    num = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    if len(sys.argv) > 1:
        print google_it(sys.argv[1], num)
    else:
        print google_it("ya.ru", 10)
