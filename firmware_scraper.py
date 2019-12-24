#!/usr/bin/env python

"""
Firmware brute force scraper
Swisscom please make an index available -_-'
Instead of having to do random bs like this,
just because you support can't give us the links
and please add a checkbox to stop auto update.
"""

import requests


def dl(url, file):
    print(url)
    r = requests.get(url)
    print(r.status_code)
    if r.status_code == 200:
        open(file, "wb").write(r.content)


v = "ibp_ap_10-{}-{}.acs"

for j in range(3, 5):
    j = "{:0>2}".format(j)
    for i in range(47, 100):
        i = "{:0>2}".format(i)
        version = v.format(j, i)
        url = f"https://www.swisscom.ch/dam/swisscom/de/biz/sme/public/hilfe/{version}"
        dl(url, version)
