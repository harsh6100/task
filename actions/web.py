import requests as req
import webbrowser as web

resp = req.get("http://www.github.com")

print(resp.status_code)
print(resp.history)
print(resp.url)
resp.url
web.open("http://www.github.com")
