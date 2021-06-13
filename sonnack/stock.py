#http://theautomatic.net/2018/01/25/coding-yahoo_fin-package/

from yahoo_fin.stock_info import get_data

amazon_weekly= get_data("nflx")
print(amazon_weekly)

