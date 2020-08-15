import requests

url = 'http://httpbin.org/redirect-to'
payload = {'url':'www.google.com'}
res = requests.get(url,params=payload)

print(str(res.status_code))

for x in res.history:
    print(x.status_code, x.url)
