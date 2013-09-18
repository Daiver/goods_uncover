
from sys import argv
import zbar
from PIL import Image
import zgoogle
import name_extractor

#if __name__ == '__main__':
def barcode_search(imgname):
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    pil = Image.open(imgname).convert('L')
    width, height = pil.size
    raw = pil.tostring()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
    sym = None
    for symbol in image:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        sym = symbol.data
    data = zgoogle.google_it(u'%s' % sym, 20)
    text = reduce(lambda x, y: x + y, map(name_extractor.normalize_text, map(lambda x: x[0] + ' ' + x[1], data)))
    dct = name_extractor.get_freq_dict(text)
    '''lst = [(dct[x], x) for x in dct]
    lst.sort()
    for x in lst:
        print x[0], x[1]'''

    return name_extractor.filter_good_name(dct)

if __name__ == '__main__':
    print barcode_search(argv[1])
