from __future__ import with_statement
import contextlib
import PySimpleGUI as sg
#import urllib.request
#import json
layout = [
              [sg.Text('Please enter url:')],
              [sg.Text('url', size=(15, 1)), sg.InputText()],
              [sg.Submit(bind_return_key=True)],[sg.Text('short url :', size=(15, 1))],[sg.Text('', size=(15, 1), key='out')]]
window = sg.Window('url shortner', layout)

#ey = "Enter your API"#enter your API key

try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import sys


def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')
while True:

	event, values = window.Read()
	x= make_tiny(values[0])
	print(x)
	window.Element('out').Update(x)
window.Close()
