from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain"]
variable = pytrends.top_charts('2021', hl='en-US', tz=300, geo='GLOBAL')

print(variable)