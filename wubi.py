# coding: utf-8
import console
import sys
from markdown2 import markdown
import ui
import requests

TEMPLATE = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Preview</title>
<style type="text/css">
body {
	font-family: helvetica;
	font-size: 15px;
	margin: 10px;
}
</style>
</head>
<body>{{CONTENT}}</body>
</html>
'''

def main():
	
	search_word = console.input_alert(u'想查哪个字的编码？')
	if not search_word:
		print('No text input found.')
		sys.exit(0)
	
	url = "https://www.iamwawa.cn/home/wubi/ajax"
	
	headers = {
		'Origin': 'https://www.iamwawa.cn',
		'Referer': 'https://www.iamwawa.cn/wubi.html',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
		}
		
	payload = {"hanzi": search_word}
		
	response = requests.post(url,headers=headers, data=payload)
	
	res_dict = {}
	if response.status_code == 200:
		data = response.json()
			
		if data['status'] == 1:
			res_dict = data['data'][0]
			
		else:
			print(response.json())
	else:
		print('请求异常')
		print(response.json())
		sys.exit(1)
	

	text = "# {}\n - 98简码: {}\n - 98编码: {}\n - 拼音: {}\n\n![](https://iamwawa.cn/Data/wubi/{}.png)".format(search_word,res_dict["c98j"],res_dict["c98"],res_dict["py"],search_word)
	converted = markdown(text)
	html = TEMPLATE.replace('{{CONTENT}}', converted)
	webview = ui.WebView(name='98五笔编码查询')
	webview.load_html(html)
	webview.present()

if __name__ == '__main__':
	main()
