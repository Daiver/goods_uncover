from grab import Grab

pageaddr = 'http://yandex.ru/yandsearch?lr=193&text=4710937382310' 
pageaddr = 'http://market.yandex.ru/model.xml?text=4710937382310&srnum=4&modelid=7880758&hid=91491' 
pageaddr = 'http://market.yandex.ru/product/7880758/reviews'
pageaddr ='http://google.com/search?hl=en&as_q=%s&num=%s&as_qdr=%s'%('4710937382310',str(10),'')
#pageaddr = 'http://www.google.ru/?q=4710937382310#newwindow=1&psj=1&q=4710937382310' 

print pageaddr
exit()
g = Grab(log_file='out.html')
g.go(pageaddr)
#print g.xpath_text('//a[@class="b-serp-item__title-link"]')
#print g.xpath_text('//h3')
print g.doc.select('//h3').one()
