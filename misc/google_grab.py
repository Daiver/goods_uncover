from grab import Grab

def google_it(q, num):
    pageaddr ='http://google.com/search?hl=en&as_q=%s&num=%s&as_qdr=%s'%(q, str(num),'')
    g = Grab()
    g.go(pageaddr)
    titles = g.doc.select('//div/h3').text_list()
    hrefs = g.doc.select('//div/h3/a/@href').text_list()
    return zip(titles, hrefs)

print google_it("ya.ru", 10)
