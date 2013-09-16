import re
import os
import sys
import urllib2
from random import random
from time import time
import lxml.html
from commands import *

#pageaddr = 'https://www.google.ru/?q=%s' % ('4710937382310')
#pageaddr = 'https://www.google.ru/?q=4710937382310#newwindow=1&psj=1&q=4710937382310' 
pageaddr = 'http://yandex.ru/yandsearch?lr=193&text=4710937382310' 

print pageaddr

page = urllib2.urlopen(pageaddr)
html = page.read()
doc = lxml.html.document_fromstring(html)
print html
