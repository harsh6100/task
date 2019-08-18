#!/usr/bin/env python

import requests as req
import webbrowser as web

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
		resp = requests.get(url)
		print(resp.status_code)
		print(resp.history)
		print(resp.url)
		web.open("http://www.github.com")
