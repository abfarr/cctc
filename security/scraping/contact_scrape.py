import lxml.html
import requests

page = requests.get('http://192.168.28.111/sites/NSC-Contacts.html')
tree = lxml.html.fromstring(page.content)

flag_parts = tree.xpath('//td[@class="f1aG"]/node()')
flag_parts = [i.text_content() if isinstance(i, lxml.html.HtmlElement) else i for i in flag_parts]

for i in range(0, len(flag_parts), 2):
	print("{}: {}".format(flag_parts[i], flag_parts[i+1]))
