# Google Weather
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession

s = HTMLSession()

query = 'los+angeles'
url = f'http://www.google.com/search?q=weather+{query}'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
r = s.get(url, headers=headers)

temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
condition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(query, temp, unit, condition)