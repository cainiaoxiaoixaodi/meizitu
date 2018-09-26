import requests

url = 'http://www.meizitu.com/a/more_1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

data = requests.get(url, headers=headers)
print(data.content.decode('GBK'))
