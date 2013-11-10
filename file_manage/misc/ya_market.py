import sys
from grab import Grab
import grab

def ym_search(q): #fix it!
    pageaddr ='http://market.yandex.ru/search.xml?text=%s' % ('+'.join(q.split()))
    #print pageaddr
    g = Grab()
    g.go(pageaddr)
    try:
        #print g.doc.select('//div').text_list()
        title = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a').text()
        href = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a/@href').text()
        modelid = href[href.find('modelid=') + len("modelid="):href.find('&hid')]
        return (title, modelid, 'http://market.yandex.ru' + href)
    except grab.error.DataNotFound as e:
        return ()

def ym_review(modelid):
    pageaddr = "http://market.yandex.ru/product/%s/reviews" % modelid
    g = Grab()
    g.go(pageaddr)

    comments = g.doc.select('//div[@class="b-aura-review b-aura-review_collapsed js-review js-review-model"]/@id')
    res = []
    for c in comments.text_list():
        names = g.doc.select('//div[@id="%s"]//*[@class="b-aura-username"]' % c).text_list()
        name = names[0] if len(names) > 0 else 'Unkn'
        ans = '\n'.join(g.doc.select('//div[@id="%s"]//*[@class="b-aura-review__verdict"]' % c).text_list())
        res.append([name, ans])
    
    return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ym_search(sys.argv[1])
    else:
        ans = ym_search("4710937382310")
        print ans
        ans2 = ym_review(ans[1])
        #print ans
        for x in ans2: 
            try:
                print x
                #print '>>>>', x[0]
                #print x[1]
            except Exception as e:
                print e
        
        #print ym_search("47109370")
        #print ym_search("4605922006695")
