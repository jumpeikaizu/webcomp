# -*- coding: utf-8 -*-
import sys
import urllib
import json
reload(sys)
sys.setdefaultencoding("utf-8")

def geocoding(address):
    url = urllib.urlopen(
        "http://maps.google.com/maps/api/geocode/json?%s" %
        urllib.urlencode(
            {"address":address,
             #"components":"country:jp",
             "sensor":"false",
             "language":"ja"
             })
        )
    result = json.loads(url.read())
    if result["status"] == "ZERO_RESULTS":
        return 0
    japan = {u'long_name': u'日本', u'types': [u'country', u'political'], u'short_name': u'JP'}
    if japan in result["results"][0]["address_components"]:
        #return result
        return result["results"][0]["geometry"]["location"]
    else:
        return 0
    
if "__main__" == __name__:
    print geocoding(sys.argv[1].encode("utf-8"))
