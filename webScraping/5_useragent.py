import requests

res = requests.get("http://www.jiheon.shop")
res.raise_for_status()

with open("scrapping.html", "w", encoding='utf-8') as f:
    f.write(res.text)