import sys
from grab import Grab
import grab

def sf_search(name):
    def head_or_none(l): return None if len(l) == 0 else l[0]
    name = name.replace(' ', '+')
    # l-catalog-item
    pageaddr = "http://www.sotmarket.ru/search/?ref=7&q=%s" % name
    g = Grab()
    g.go(pageaddr)
    #items = g.doc.select('//li[@class="l-catalog-item"]')
    #b-sbutton mod_price skin_product size_normal scheme_available
    items = g.doc.select('//li[@class="l-catalog-item"]/div/div[@class="b-catalog_goods-link"]').text_list()
    price = g.doc.select('//li[@class="l-catalog-item"]/div/span[@class="b-sbutton mod_price skin_product size_normal scheme_available"]').text_list()
    href = g.doc.select('//li[@class="l-catalog-item"]/div/div[@class="b-catalog_goods-link"]/a/@href').text_list()

    return map(head_or_none, [items, price, href])

def sf_reviews(href):
    href = 'http://www.sotmarket.ru%s#tab=opinions' % href
    print href

if __name__ == '__main__':
    res = sf_search('htc one s')
    print res
    print sf_reviews(res[2])
