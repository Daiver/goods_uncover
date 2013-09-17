import sys
from grab import Grab

def ym_search(q):
    #pageaddr ='http://google.com/search?hl=en&as_q=%s&num=%s&as_qdr=%s' % ('+'.join(q.split()), str(num),'')
    pageaddr ='http://market.yandex.ru/search.xml?text=%s' % ('+'.join(q.split()))
    print pageaddr
    g = Grab()
    g.go(pageaddr)
    title = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a').text()
    href = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a/@href').text()
    print title
    print href

    #hrefs = g.doc.select('//div/h3/a/@href').text_list()
    #return zip(titles, hrefs)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ym_search(sys.argv[1])
    else:
        print ym_search("4710937382310")
        #print ym_search("4605922006695")
