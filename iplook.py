import requests  

url = "http://myip.ipip.net/"  
header = {  
    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"  
}  

resp = requests.get(url=url, verify=False, headers=header)  
resp.encoding = "utf-8"  
print(resp.text)