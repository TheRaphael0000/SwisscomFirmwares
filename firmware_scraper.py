#!/usr/bin/env python

# Firmware brute force scraper
# Swisscom please build make the index available -_-'
# Instead of having to do random bs like this, just because you support can't give us the links

import os

def check(url):
	c = "curl -s -o /dev/null -w \"%{http_code}\" " + url
	result = os.popen(c).read()
	return result

def dl(url, file):
	os.system(f"curl --output {file} {url}")

# NOTE: version check https://www.swisscom.ch/en/residential/help/internet/firmware-aktualisierungen-fuer-ihre-internet-box.html
# Can be improve to avoid double download (with the check and dl)

for j in range(0,4):
	j = "{:0>2}".format(j)
	for i in range(0,100):
		i = "{:0>2}".format(i)
		version = f"wb_10-{j}-{i}.rui"

		url = f"https://www.swisscom.ch/dam/swisscom/de/biz/sme/public/hilfe/{version}"
		print(url)
		hc = check(url)
		print(hc)
		if hc == "200":
			dl(url, version)
