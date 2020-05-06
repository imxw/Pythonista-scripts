import requests
import urllib
import hashlib
import sys
import json
import console

url = "http://www.xhup.club/Xhup/Search/searchCode"

search_word = console.input_alert(u'想查哪些字的编码？')
if not search_word:
    print('No text input found.')
    sys.exit(0)

key_xhup = 'fjc_xhup'

search_word_url = urllib.parse.quote(search_word)

ret = key_xhup + search_word
sign = hashlib.md5((ret).encode('utf-8')).hexdigest()

payload = 'search_word={}&sign={}'.format(search_word_url, sign)
headers = {
  'Origin': 'http://react.xhup.club',
  'Referer': 'http://react.xhup.club/search',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
  'Host': 'www.xhup.club',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Accept': 'application/json, text/plain, */*'
}

response = requests.request("POST", url, headers=headers, data = payload)

if response.status_code == 200:
    data = response.json()
    if data['msg'] == 'success':
        list_dz = data['list_dz']
        # print(json.dumps(list_dz, ensure_ascii=False, indent=2))
        for x in list_dz:
            print(x[0])
            print('● 拆分：{}'.format(x[1]))
            print('● 首末：{} {}'.format(x[2], x[3]))
            print('● 形码：{} {}'.format(x[4], x[5]))
            print('--------------------')
    else:
        print(response.json())
else:
    print('请求异常')
    print(response.json())
    sys.exit(1)
    
