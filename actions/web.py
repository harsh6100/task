#!/usr/bin/env python

import requests as req
import webbrowser as web

from st2common.runners.base_action import Action

def run(self, url):
	res = req.get(url)

print(res.status_code)
print(res.history)
print(res.url)
res.url
web.open("http://www.github.com")
