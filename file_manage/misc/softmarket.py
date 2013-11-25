import sys
from grab import Grab
import grab

def sf_search(name):
    name = name.replace(' ', '+')
    # l-catalog-item
    pageaddr = "http://www.sotmarket.ru/search/?ref=7&q=%s" % name
    g = Grab()
    g.go(pageaddr)
    #items = g.doc.select('//li[@class="l-catalog-item"]')
    items = g.doc.select('//li[@class="l-catalog-item"]/div/div[@class="b-catalog_goods-link"]').text_list()
    item_name = None if len(items) == 0 else items[0]

    return (item_name)
    '''for x in items.text_list():
        try:
            print x
        except:
            pass'''

if __name__ == '__main__':
    print sf_search('htc one s')
