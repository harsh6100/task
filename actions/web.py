import requests as req
import webbrowser as web

from st2common.runners.base_action import Action

resp = req.get(url)

print(resp.status_code)
print(resp.history)
print(resp.url)
resp.url
web.open("http://www.github.com")
