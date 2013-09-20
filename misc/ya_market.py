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

    def make_groups(lst):
        res = []
        i = 2
        while i < len(lst):
            res.append([lst[i - 2], lst[i - 1], lst[i]])
            i += 3
        return res

    #comments = g.doc.select('//div[@class="b-aura-review__verdict"]')
    comments = g.doc.select('//div[@class="b-aura-review b-aura-review_collapsed js-review js-review-model"]')
    for c in comments:
        print c.select('//div/*[class="b-aura-username"]').text_list()
        #s = c.select('//*[@class="b-aura-username"]').text()
        #print s
        #print c.text()
        #for x in c.text_list(): print x
    #print dir(comments [0])
    print dir(comments)
    exit()
    #comments = make_groups(comments)
    names = g.doc.select('//div/*[@class="b-aura-username"]').text_list()
    for x in names: print x
    print len(names), len(comments)
    #return zip(names, comments)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ym_search(sys.argv[1])
    else:
        ans = ym_search("4710937382310")
        ans2 = ym_review(ans[1])
        print ans
        for x in ans2: 
            print '>>>>', x[0]
            for y in x[1]:
                print y
        
        #print ym_search("47109370")
        #print ym_search("4605922006695")
