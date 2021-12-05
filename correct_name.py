import sys
import os

coin = sys.argv[1].upper()
ext = ".svg" 

os.rename("svg/{}{}".format(coin, ext), 'svg/{}2{}'.format(coin, ext))
os.rename("svg/{}-alt{}".format(coin, ext), 'svg/{}{}'.format(coin, ext))
os.rename("svg/{}2{}".format(coin, ext), 'svg/{}-alt{}'.format(coin, ext))