
from sys import argv
import zbar
from PIL import Image
import zgoogle
import name_extractor
import ya_market

#if __name__ == '__main__':

def google_barcode_search(sym):
    data = zgoogle.google_it(u'%s' % sym, 20)
    text = reduce(lambda x, y: x + y, map(name_extractor.normalize_text, map(lambda x: x[0] + ' ' + x[1], data)))
    dct = name_extractor.get_freq_dict(text)
    lst = [(dct[x], x) for x in dct]
    lst.sort()
    for x in lst:
        print x[0], x[1]

    return name_extractor.filter_good_name(dct)


def barcode_search(imgname):
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    pil = Image.open(imgname).convert('L')
    width, height = pil.size
    raw = pil.tostring()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
    sym = None
    tp = None
    ans = None
    name = None
    for symbol in image:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        if str(symbol.type) == 'EAN13':
            sym = symbol.data

    if None == sym: return []
    ya_ans = ya_market.ym_search(sym)
    if len(ya_ans) == 0:
        ans = google_barcode_search(sym)
        tp = 'google'
    else:
        ans = ya_market.ym_review(ya_ans[1])
    return {
            'sym' : sym,
            'type' : tp,
            'name' : name,
            'ans' : ans
        }

    
if __name__ == '__main__':
    ans = barcode_search(argv[1])
    for x in ans:
        try:
            print ans[x]
        except:
            print 'cannot print'
