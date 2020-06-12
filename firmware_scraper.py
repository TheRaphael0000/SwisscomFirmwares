#!/usr/bin/env python

"""
Firmware brute force scraper
Swisscom please make an index available -_-'
Instead of having to do random bs like this,
just because you support can't give us the links
and please add a checkbox to stop auto update.
"""

from urllib.request import urlopen
from urllib.error import HTTPError

file = "ibp_np_10-{}-{}.rui"
swisscom = "https://www.swisscom.ch/dam/swisscom/de/biz/sme/public/hilfe/{}"

for j in range(0, 5):
    j = "{:0>2}".format(j)
    for i in range(0, 100):
        i = "{:0>2}".format(i)
        version = file.format(j, i)
        url = swisscom.format(version)

        try:
            r = urlopen(url)
            code = r.getcode()
            if code == 200:
                print(url)
        except HTTPError:
            pass
