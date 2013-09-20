import sys
from grab import Grab

def ym_search(q): #fix it!
    #pageaddr ='http://google.com/search?hl=en&as_q=%s&num=%s&as_qdr=%s' % ('+'.join(q.split()), str(num),'')
    pageaddr ='http://market.yandex.ru/search.xml?text=%s' % ('+'.join(q.split()))
    #print pageaddr
    g = Grab()
    g.go(pageaddr)
    try:
        title = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a').text()
        href = g.doc.select('//div[@class="b-offers b-offers_type_guru b-offers_type_guru_mix"]/div/h3/a/@href').text()
        modelid = href[href.find('modelid=') + len("modelid="):href.find('&hid')]
        return (title, modelid, 'http://market.yandex.ru' + href)
    except grab.error.DataNotFound as e:
        return ()
    #print title
    #print href

    #hrefs = g.doc.select('//div/h3/a/@href').text_list()
    #return zip(titles, hrefs)

def ym_review(modelid):
    pageaddr = "http://market.yandex.ru/product/%s/reviews" % modelid
    g = Grab()
    g.go(pageaddr)
    try:
        res = g.doc.select('//div[@class="b-aura-review__verdict"]/div').text_list()
        def make_groups(lst):
            res = []
            i = 2
            while i < len(lst):
                res.append([lst[i - 2], lst[i - 1], lst[i]])
                i += 3
            return res

        return make_groups(res)
        
    except:
        return []

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ym_search(sys.argv[1])
    else:
        ans = ym_search("4710937382310")
        ans2 = ym_review(ans[1])
        print ans
        for x in ans2: 
            print '>>>>'
            for y in x:
                print y
        
        #print ym_search("47109370")
        #print ym_search("4605922006695")
